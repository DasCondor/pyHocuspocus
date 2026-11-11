'use strict';

const $ = id => document.getElementById(id);

const SUITS = ['♠', '♥', '♣', '♦'];
const SUIT_NAMES = ['Spades', 'Hearts', 'Clubs', 'Diamonds'];
const RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
const RANK_NAMES = { A: 'Ace', J: 'Jack', Q: 'Queen', K: 'King' };
const PILE_NUMERALS = ['I', 'II', 'III'];
const ROUNDS = 3;

const INTRO_TEXT =
  'Choose any card in your mind. Keep it a secret.<br>' +
  'Tell me only which pile holds it. Three choices. One impossible reveal.';

const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

let deck = [];
let piles = [];
let round = 0;
let phase = 'remember'; // 'remember' -> 'choose' -> 'reveal'
let busy = false;
let soundOn = false;
let audio;
let generation = 0; // bumped on reset so in-flight animations can bail out

/* ---------- The trick ---------- */

function shuffle(cards) {
  for (let i = cards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cards[i], cards[j]] = [cards[j], cards[i]];
  }
  return cards;
}

function newDeck() {
  const all = SUITS.flatMap((suit, s) =>
    RANKS.map((rank, r) => ({
      id: s * 13 + r,
      rank,
      suit,
      red: s % 2 === 1,
      label: `${RANK_NAMES[rank] || rank} of ${SUIT_NAMES[s]}`,
    }))
  );
  return shuffle(all).slice(0, 21);
}

// Deal the cards one at a time into three piles of seven.
function deal(cards) {
  return [0, 1, 2].map(pile => cards.filter((_, i) => i % 3 === pile));
}

// Pick the piles back up with the chosen pile in the middle. The order of
// the other two doesn't matter, so it's randomised to hide the pattern.
function collect(groups, chosen, swapOthers = false) {
  const others = [0, 1, 2].filter(i => i !== chosen);
  if (swapOthers) others.reverse();
  return [...groups[others[0]], ...groups[chosen], ...groups[others[1]]];
}

/* ---------- Rendering ---------- */

function cardMarkup(card) {
  const corner = `${card.rank}<small>${card.suit}</small>`;
  return `
    <div class="face">
      <div class="corner">${corner}</div>
      <div class="pip">${card.suit}</div>
      <div class="corner bottom">${corner}</div>
    </div>
    <div class="back">✧</div>`;
}

function placeCard(el, row) {
  el.style.transform = `translate3d(0, ${row * 25}px, ${row * 0.8}px) rotateY(0deg)`;
  el.style.opacity = 1;
}

function render(animate = false) {
  const container = $('piles');
  container.innerHTML = '';

  piles.forEach((group, p) => {
    const pile = document.createElement('section');
    pile.className = 'pile';
    pile.innerHTML = `
      <div class="pile-label">PILE ${PILE_NUMERALS[p]}</div>
      <div class="cards"></div>
      <button class="select">My card is here <kbd>${p + 1}</kbd></button>`;

    const cards = pile.querySelector('.cards');
    group.forEach((card, row) => {
      const el = document.createElement('div');
      el.className = card.red ? 'card red' : 'card';
      el.setAttribute('aria-label', card.label);
      el.innerHTML = cardMarkup(card);
      el.style.zIndex = row + 1;

      if (animate) {
        // Start face down at the centre of the table, then fly into place.
        el.style.transform = `translate3d(${(1 - p) * 160}px, 80px, 60px) rotateY(180deg)`;
        el.style.opacity = 0;
        el.style.transitionDelay = `${(row * 3 + p) * 24}ms`;
        requestAnimationFrame(() => requestAnimationFrame(() => placeCard(el, row)));
      } else {
        placeCard(el, row);
      }
      cards.append(el);
    });

    const button = pile.querySelector('.select');
    button.disabled = phase !== 'choose' || busy;
    button.onclick = () => choose(p);
    container.append(pile);
  });
}

function gatherCards() {
  document.querySelectorAll('.pile').forEach((pile, p) => {
    pile.querySelectorAll('.card').forEach((el, row) => {
      el.style.transitionDelay = `${row * 22}ms`;
      el.style.transform =
        `translate3d(${(1 - p) * 160}px, 80px, ${40 + row}px) ` +
        `rotateY(180deg) rotateZ(${p * 3 - 3}deg)`;
    });
  });
}

function setStep(n) {
  [1, 2, 3].forEach(i => $('s' + i).classList.toggle('active', i === n));
}

function setPileButtonsDisabled(disabled) {
  document.querySelectorAll('.select').forEach(b => { b.disabled = disabled; });
}

function addSparkles(count) {
  for (let i = 0; i < count; i++) {
    const spark = document.createElement('i');
    spark.className = 'spark';
    spark.style.left = `${5 + Math.random() * 90}%`;
    spark.style.top = `${Math.random() * 90}%`;
    spark.style.animationDelay = `${Math.random() * 5}s`;
    spark.style.opacity = Math.random() * 0.5;
    $('table').append(spark);
  }
}

/* ---------- Sound ---------- */

function tone(freq = 440) {
  if (!soundOn) return;
  try {
    audio ??= new (window.AudioContext || window.webkitAudioContext)();
    audio.resume();
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.type = 'sine';
    osc.frequency.value = freq;
    gain.gain.setValueAtTime(0.045, audio.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audio.currentTime + 0.35);
    osc.connect(gain);
    gain.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.35);
  } catch {
    // Audio is a nicety; the game works without it.
  }
}

/* ---------- Game flow ---------- */

const wait = ms => new Promise(resolve => setTimeout(resolve, reducedMotion ? 30 : ms));

function reset() {
  generation++;
  busy = false;
  phase = 'remember';
  round = 0;
  deck = newDeck();
  piles = deal(deck);

  $('reveal').classList.remove('show');
  $('start').hidden = false;
  $('start').textContent = 'I have my card →';
  $('restart').hidden = true;
  $('status').textContent = 'Take your time. Remember one card below.';
  $('hint').textContent = 'No need to click your card. Just remember it.';
  $('instruction').innerHTML = INTRO_TEXT;
  setStep(1);
  render(true);
}

function startChoosing() {
  phase = 'choose';
  setStep(2);
  $('start').hidden = true;
  $('restart').hidden = false;
  $('status').textContent = `Round 1 of ${ROUNDS} · Which pile contains your card?`;
  $('hint').textContent = 'Select a pile below the cards, or press 1, 2, or 3.';
  setPileButtonsDisabled(false);
  tone(440);
}

async function choose(pileIndex) {
  if (phase !== 'choose' || busy) return;
  busy = true;
  setPileButtonsDisabled(true);

  const token = generation;
  round++;
  tone(330 + round * 110);
  $('status').textContent = round === ROUNDS
    ? 'The last pieces fall into place…'
    : 'Gathering the cards. Keep your card in mind…';

  gatherCards();
  deck = collect(piles, pileIndex, Math.random() > 0.5);
  await wait(1150);
  if (token !== generation) return;

  if (round === ROUNDS) {
    reveal();
    return;
  }

  piles = deal(deck);
  render(true);
  $('status').textContent = `Round ${round + 1} of ${ROUNDS} · Find your same card again.`;
  await wait(1450);
  if (token !== generation) return;

  busy = false;
  setPileButtonsDisabled(false);
}

function reveal() {
  // After three rounds the remembered card is always the 11th in the deck.
  const card = deck[10];

  phase = 'reveal';
  setStep(3);
  $('hero').innerHTML = `<div class="${card.red ? 'card red' : 'card'}">${cardMarkup(card)}</div>`;
  $('answer').textContent = card.label;
  $('reveal').classList.add('show');
  $('status').textContent = 'Was that your card?';
  $('instruction').innerHTML = 'Three choices brought us here.<br>A secret you never had to tell.';
  $('start').textContent = 'Try another card ↻';
  $('start').hidden = false;
  $('hint').textContent = 'Always follow the same card for the illusion to work.';
  $('restart').hidden = true;
  tone(880);
  busy = false;
}

/* ---------- Controls ---------- */

$('start').onclick = () => (phase === 'reveal' ? reset() : startChoosing());
$('restart').onclick = reset;

$('sound').onclick = () => {
  soundOn = !soundOn;
  $('sound').textContent = soundOn ? 'Sound on' : 'Sound off';
  $('sound').setAttribute('aria-pressed', soundOn);
  tone();
};

$('help').onclick = () => $('helpDialog').showModal();
$('closeHelp').onclick = () => $('helpDialog').close();

document.addEventListener('keydown', e => {
  if (!$('helpDialog').open && ['1', '2', '3'].includes(e.key)) {
    choose(Number(e.key) - 1);
  }
});

addSparkles(18);
reset();
