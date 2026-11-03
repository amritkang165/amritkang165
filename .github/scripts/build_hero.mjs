// Rebuild the self-contained animated header after replacing the JPEG poster.
// The embedded image is required: external images do not load inside an SVG <img>.
// Run from any directory: node .github/scripts/build_hero.mjs
import { readFile, writeFile } from 'node:fs/promises';

const assets = new URL('../../assets/after-hours/', import.meta.url);
const poster = await readFile(new URL('amrit-hero-effects.jpg', assets));
const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="2172" height="724" viewBox="0 0 2172 724" role="img" aria-labelledby="title desc">
  <title id="title">Amrit Kang / After Hours — Ideas loud. Code louder.</title>
  <desc id="desc">Amrit's face portrait beside a rear-view JATT KANG shirt photo, with blue trails and orange rim lighting. Full-stack, iOS, AI engineering and open source specialisations. Blue and orange signals travel around the frame and constellation accents pulse; the photos and text remain still.</desc>
  <style>
    .frame-signal { animation: orbit-frame 22s linear infinite; }
    .blue-signal { animation: orbit-frame 28s linear infinite reverse; }
    .stars { animation: star-pulse 7s ease-in-out infinite; }
    .reticle { transform-origin: 58px 46px; animation: rotate-reticle 18s linear infinite; }
    .accent { animation: breathe 6s ease-in-out infinite; }
    @keyframes orbit-frame { to { stroke-dashoffset: -5736; } }
    @keyframes rotate-reticle { to { transform: rotate(360deg); } }
    @keyframes breathe { 0%,100% { opacity: .35; } 50% { opacity: .95; } }
    @keyframes star-pulse { 0%,100% { opacity: .25; } 50% { opacity: .85; } }
    @media (prefers-reduced-motion: reduce) {
      .frame-signal, .blue-signal, .stars, .reticle, .accent { animation: none; }
    }
  </style>
  <image width="2172" height="724" href="data:image/jpeg;base64,${poster.toString('base64')}"/>
  <rect x="8" y="8" width="2156" height="708" fill="none" stroke="#ff6a2b" stroke-opacity=".22" stroke-width="2"/>
  <rect class="frame-signal" x="8" y="8" width="2156" height="708" pathLength="5736" fill="none" stroke="#ff6a2b" stroke-width="5" stroke-linecap="round" stroke-dasharray="160 2708"/>
  <rect class="blue-signal" x="8" y="8" width="2156" height="708" pathLength="5736" fill="none" stroke="#45c9ff" stroke-width="3" stroke-linecap="round" stroke-dasharray="90 5646" stroke-dashoffset="-1700"/>
  <g class="stars" fill="#a7eaff">
    <circle cx="1550" cy="198" r="3"/><circle cx="1598" cy="218" r="3"/>
    <circle cx="1625" cy="175" r="3.5"/><circle cx="1670" cy="155" r="3"/>
    <circle cx="1710" cy="136" r="3"/><circle cx="2090" cy="118" r="3.5"/>
    <circle cx="2070" cy="136" r="3"/><circle cx="2046" cy="180" r="3"/>
  </g>
  <g class="reticle" fill="none" stroke="#ff6a2b" stroke-width="3">
    <circle cx="58" cy="46" r="29" stroke-dasharray="21 70"/>
    <circle cx="87" cy="46" r="3" fill="#ff6a2b" stroke="none"/>
  </g>
  <g class="accent" stroke="#ff6a2b" stroke-width="3" fill="none">
    <path d="M26 614v-24h24M2100 154h24v24"/>
    <path d="M1080 15h24v24"/>
  </g>
</svg>
`;
await writeFile(new URL('amrit-hero-animated.svg', assets), svg);
console.log(`Built amrit-hero-animated.svg (${Math.round(Buffer.byteLength(svg) / 1024)} KiB)`);
