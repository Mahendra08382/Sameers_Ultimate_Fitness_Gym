import streamlit as st

st.set_page_config(
    page_title="Sameer's Ultimate Fitness & Gym",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;600;700&family=Rajdhani:wght@400;500;600&display=swap');
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp { background: #0a0a0a !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
* { box-sizing: border-box; }

.stButton > button {
    background: linear-gradient(135deg, #dc2626, #991b1b) !important;
    color: white !important;
    font-family: 'Oswald', sans-serif !important;
    font-size: 1rem !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 14px 40px !important;
    width: 100% !important;
}
.stTextInput input, .stTextArea textarea {
    background: #1a1a1a !important;
    color: #fff !important;
    border: 1px solid #374151 !important;
    border-radius: 6px !important;
    font-size: 1rem !important;
}
.stSelectbox > div > div {
    background: #1a1a1a !important;
    color: #fff !important;
    border: 1px solid #374151 !important;
}
label { color: #9ca3af !important; font-family: 'Oswald', sans-serif !important; }
div[data-testid="stForm"] {
    background: #111 !important;
    border: 1px solid #1f2937 !important;
    border-top: 3px solid #dc2626 !important;
    border-radius: 10px !important;
    padding: 20px !important;
}

@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
@keyframes glow { 0% { box-shadow: 0 0 30px rgba(220,38,38,0.5); } 100% { box-shadow: 0 0 70px rgba(220,38,38,0.9); } }
@keyframes fadeup { from { opacity:0; transform:translateY(30px); } to { opacity:1; transform:translateY(0); } }

.nav-links-desktop { display: flex; gap: 20px; }
.nav-links-mobile { display: none; }

.hero-buttons-wrap { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px; }
.hero-btn-primary {
    background: linear-gradient(135deg,#dc2626,#991b1b);
    color: #fff; font-family: Oswald,sans-serif; font-size: 0.95rem;
    letter-spacing: 2px; text-transform: uppercase;
    padding: 14px 28px; border-radius: 4px; text-decoration: none;
    border: 2px solid #dc2626; display: inline-block;
}
.hero-btn-secondary {
    background: transparent; color: #fff;
    font-family: Oswald,sans-serif; font-size: 0.95rem;
    letter-spacing: 2px; text-transform: uppercase;
    padding: 14px 28px; border-radius: 4px; text-decoration: none;
    border: 2px solid #fff; display: inline-block;
}

.stats-row { display: flex; justify-content: center; flex-wrap: wrap; }
.stat-box { text-align: center; padding: 10px 20px; border-right: 1px solid #374151; }
.stat-box:last-child { border-right: none; }

.grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; max-width: 1000px; margin: 0 auto; }
.grid-3col { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; max-width: 1050px; margin: 0 auto; }
.grid-4col { display: grid; grid-template-columns: repeat(4, 1fr); max-width: 900px; margin: 0 auto; background: #0a0a0a; border-radius: 12px; overflow: hidden; border: 1px solid #1f2937; }
.grid-auto { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; max-width: 1150px; margin: 0 auto; }
.grid-contact { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; max-width: 1000px; margin: 0 auto 50px; }

.about-card { flex: 0 0 280px; min-width: 250px; }
.about-text { flex: 1; min-width: 280px; }

.sched-row { display: grid; grid-template-columns: 1.5fr 1.5fr 1.5fr 1fr; }
.sched-header { background: linear-gradient(135deg,#dc2626,#991b1b); }

.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; max-width: 1050px; margin: 0 auto; align-items: start; }

.why-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 1100px; margin: 0 auto; }

.footer-links-row { display: flex; justify-content: center; gap: 22px; flex-wrap: wrap; margin-bottom: 25px; }
.footer-info-row { display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; margin-bottom: 25px; }

.cta-btns { display: flex; gap: 18px; justify-content: center; flex-wrap: wrap; }

@media (max-width: 768px) {
    .nav-links-desktop { display: none !important; }
    .grid-2col { grid-template-columns: 1fr !important; gap: 25px !important; }
    .grid-3col { grid-template-columns: 1fr !important; }
    .grid-4col { grid-template-columns: repeat(2, 1fr) !important; }
    .grid-auto { grid-template-columns: 1fr !important; }
    .grid-contact { grid-template-columns: repeat(2, 1fr) !important; }
    .about-card { flex: none !important; width: 100% !important; min-width: unset !important; }
    .about-text { min-width: unset !important; }
    .stat-box { padding: 10px 12px !important; border-right: none !important; border-bottom: 1px solid #374151 !important; }
    .stat-box:last-child { border-bottom: none !important; }
    .stats-row { flex-direction: column !important; align-items: center !important; }
    .sched-row { grid-template-columns: 1fr 1fr !important; }
    .sched-header { grid-template-columns: 1fr 1fr !important; }
    .sched-cell-eve { display: none !important; }
    .sched-head-eve { display: none !important; }
    .pricing-grid { grid-template-columns: 1fr !important; }
    .why-grid { grid-template-columns: 1fr !important; }
    .footer-links-row { gap: 14px !important; }
    .hero-buttons-wrap { flex-direction: column !important; align-items: center !important; }
    .hero-btn-primary, .hero-btn-secondary { width: 260px !important; text-align: center !important; }
    .cta-btns { flex-direction: column !important; align-items: center !important; }
    .section-pad { padding: 50px 16px !important; }
    .hero-title-main { font-size: 3rem !important; }
    .hero-title-red { font-size: 4rem !important; }
    .section-title-text { font-size: 2.2rem !important; }
}

@media (max-width: 480px) {
    .grid-4col { grid-template-columns: 1fr !important; }
    .grid-contact { grid-template-columns: 1fr !important; }
    .hero-title-main { font-size: 2.5rem !important; }
    .hero-title-red { font-size: 3rem !important; }
}
</style>
""", unsafe_allow_html=True)


def divider():
    st.markdown('<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>', unsafe_allow_html=True)


def section_header(title, highlight, subtitle):
    st.markdown(
        '<div style="text-align:center;margin-bottom:40px;">'
        f'<div class="section-title-text" style="font-family:Bebas Neue,cursive;font-size:clamp(2rem,6vw,4.5rem);color:#fff;letter-spacing:4px;">'
        f'{title} <span style="color:#dc2626;">{highlight}</span>'
        '</div>'
        '<div style="width:70px;height:4px;background:linear-gradient(90deg,#dc2626,#991b1b);margin:10px auto 14px;border-radius:2px;"></div>'
        f'<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.85rem;letter-spacing:3px;text-transform:uppercase;">{subtitle}</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ── NAVBAR ──────────────────────────────────────────────────
st.markdown(
    '<div style="background:rgba(0,0,0,0.97);border-bottom:2px solid #dc2626;padding:12px 20px;'
    'display:flex;align-items:center;justify-content:space-between;box-shadow:0 4px 25px rgba(220,38,38,0.3);'
    'position:sticky;top:0;z-index:9999;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:1.5rem;color:#fff;letter-spacing:3px;">'
    'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span>'
    '</div>'
    '<div class="nav-links-desktop">'
    '<a href="#about" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">ABOUT</a>'
    '<a href="#services" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">SERVICES</a>'
    '<a href="#pricing" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">PRICING</a>'
    '<a href="#contact" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;font-weight:700;">JOIN NOW</a>'
    '</div>'
    '<div style="display:none;" class="nav-links-mobile">'
    '<a href="tel:9483834949" style="color:#dc2626;font-family:Oswald,sans-serif;font-size:0.9rem;text-decoration:none;letter-spacing:1px;">📞 CALL</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# Mobile top call bar
st.markdown(
    '<div style="background:#dc2626;padding:8px 16px;text-align:center;display:none;" id="mobile-cta">'
    '<a href="tel:9483834949" style="color:#fff;font-family:Oswald,sans-serif;font-size:0.9rem;text-decoration:none;letter-spacing:2px;">📞 TAP TO CALL: 9483834949</a>'
    '</div>'
    '<style>@media(max-width:768px){#mobile-cta{display:block!important;}}</style>',
    unsafe_allow_html=True
)

# ── HERO ────────────────────────────────────────────────────
st.markdown(
    '<div id="home" style="background:radial-gradient(ellipse at top,#1a0000 0%,#000 50%,#050505 100%);'
    'min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center;'
    'text-align:center;padding:50px 16px 40px;">'

    '<div style="background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;'
    'font-family:Oswald,sans-serif;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;'
    'padding:7px 18px;border-radius:2px;margin-bottom:24px;">EST. 2014 — KARWAR\'S #1 FITNESS DESTINATION</div>'

    '<div style="width:140px;height:140px;border-radius:50%;'
    'background:linear-gradient(135deg,#1a1a1a,#000);border:3px solid #dc2626;'
    'display:flex;align-items:center;justify-content:center;margin:0 auto 24px auto;'
    'box-shadow:0 0 50px rgba(220,38,38,0.6);animation:glow 2s ease-in-out infinite alternate;">'
    '<div style="text-align:center;padding:8px;">'
    '<div style="font-size:1.8rem;">🏋️</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1rem;letter-spacing:2px;line-height:1.1;">SAMEER\'S</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.2rem;letter-spacing:2px;line-height:1.1;">ULTIMATE</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.45rem;letter-spacing:1px;">FITNESS &amp; GYM</div>'
    '</div>'
    '</div>'

    '<div class="hero-title-main" style="font-family:Bebas Neue,cursive;font-size:clamp(3rem,10vw,8rem);'
    'color:#fff;line-height:0.9;letter-spacing:4px;text-shadow:0 0 40px rgba(220,38,38,0.4);">FORGE YOUR</div>'
    '<div class="hero-title-red" style="font-family:Bebas Neue,cursive;font-size:clamp(3.5rem,13vw,10rem);'
    'color:#dc2626;line-height:0.9;letter-spacing:4px;text-shadow:0 0 60px rgba(220,38,38,0.7);margin-bottom:14px;">GREATNESS</div>'

    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.85rem;'
    'letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">FITNESS &amp; GYM • KARWAR, KARNATAKA</div>'

    '<div style="font-family:Rajdhani,sans-serif;color:#f3f4f6;font-size:clamp(1rem,4vw,1.4rem);'
    'font-style:italic;margin-bottom:28px;">'
    '<span style="color:#dc2626;font-size:1.8rem;">"</span>'
    'A place where champions are built'
    '<span style="color:#dc2626;font-size:1.8rem;">"</span>'
    '</div>'

    '<div class="hero-buttons-wrap">'
    '<a href="tel:9483834949" class="hero-btn-primary">📞 JOIN — 9483834949</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" class="hero-btn-secondary">📸 FOLLOW US</a>'
    '</div>'

    '<div class="stats-row">'
    '<div class="stat-box">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
    '</div>'
    '<div class="stat-box">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div class="stat-box">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">994</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '<div class="stat-box">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">100%</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Dedication</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# ── MARQUEE ─────────────────────────────────────────────────
items = ["💪 TRAIN HARD", "🔥 BURN STRONGER", "⚡ NO EXCUSES", "🏆 CHAMPIONS BUILT HERE", "💥 PUSH YOUR LIMITS", "🎯 RESULTS GUARANTEED"]
marquee_inner = ""
for item in items * 2:
    marquee_inner += f'<span style="font-family:Bebas Neue,cursive;font-size:1.1rem;color:#fff;letter-spacing:3px;padding:0 20px;">{item}</span><span style="color:rgba(255,255,255,0.4);padding:0 4px;">•</span>'

st.markdown(
    '<div style="background:linear-gradient(90deg,#dc2626,#991b1b,#dc2626);padding:12px 0;overflow:hidden;white-space:nowrap;">'
    f'<div style="display:inline-block;animation:marquee 20s linear infinite;">{marquee_inner}</div>'
    '</div>'
    '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>',
    unsafe_allow_html=True
)

# ── ABOUT ───────────────────────────────────────────────────
st.markdown('<div id="about" class="section-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("ABOUT", "US", "BUILDING CHAMPIONS SINCE 2014")
st.markdown(
    '<div class="grid-2col">'
    '<div class="about-text">'
    '<p style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.05rem;line-height:1.9;margin-bottom:18px;">'
    'Welcome to <strong style="color:#dc2626;">Sameer\'s Ultimate Fitness &amp; Gym</strong> — Karwar\'s premier '
    'fitness destination, established in 2014. For over a decade, we\'ve been transforming lives, '
    'building champions, and creating a community of unstoppable athletes.'
    '</p>'
    '<p style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.05rem;line-height:1.9;margin-bottom:24px;">'
    'Located on <strong style="color:#fff;">Kodibaga Main Road, Karwar</strong>, we offer state-of-the-art '
    'equipment, expert trainers, and an electrifying atmosphere that pushes you beyond limits every day.'
    '</p>'
    '<div style="display:flex;gap:10px;flex-wrap:wrap;">'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">YEARS</div>'
    '</div>'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">MEMBERS</div>'
    '</div>'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">100%</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">RESULTS</div>'
    '</div>'
    '</div>'
    '</div>'
    '<div class="about-card">'
    '<div style="background:linear-gradient(135deg,#1a0000,#2d0000);border:2px solid #dc2626;border-radius:12px;'
    'padding:40px 25px;text-align:center;box-shadow:0 20px 60px rgba(220,38,38,0.25);">'
    '<div style="font-size:3.5rem;margin-bottom:12px;">🏋️</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.6rem;letter-spacing:4px;">SAMEER\'S</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:2.5rem;letter-spacing:4px;line-height:1;">ULTIMATE</div>'
    '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);margin:12px 0;"></div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:4px;">FITNESS &amp; GYM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.7rem;letter-spacing:2px;margin-top:4px;">EST 2014</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── WHY CHOOSE US ───────────────────────────────────────────
st.markdown('<div class="section-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("WHY", "CHOOSE US", "WHAT MAKES US KARWAR'S BEST GYM")
why_items = [
    ("🏆", "PROVEN RESULTS", "Hundreds of success stories from real members who transformed their bodies."),
    ("💡", "EXPERT COACHING", "Certified trainers with years of experience guiding you every step."),
    ("⚙️", "MODERN EQUIPMENT", "State-of-the-art machines and free weights for the ultimate workout."),
    ("🔥", "INTENSE ATMOSPHERE", "An electrifying environment that keeps you motivated every day."),
    ("👥", "STRONG COMMUNITY", "A brotherhood of fitness enthusiasts pushing each other to excel."),
    ("📍", "PRIME LOCATION", "Conveniently located on Kodibaga Main Road, Karwar."),
]
wg = '<div class="why-grid">'
for icon, title, desc in why_items:
    wg += (
        '<div style="background:rgba(220,38,38,0.05);border:1px solid rgba(220,38,38,0.2);'
        'border-radius:10px;padding:28px 20px;text-align:center;">'
        f'<div style="font-size:2.2rem;margin-bottom:12px;">{icon}</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#fff;font-size:1rem;letter-spacing:2px;margin-bottom:8px;">{title}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.9rem;line-height:1.6;">{desc}</div>'
        '</div>'
    )
wg += '</div>'
st.markdown(wg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── SERVICES ────────────────────────────────────────────────
st.markdown('<div id="services" class="section-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("OUR", "SERVICES", "EVERYTHING YOU NEED TO REACH YOUR PEAK")
services = [
    ("🏋️", "WEIGHT TRAINING", "Comprehensive strength training with free weights, barbells, and machines for all levels."),
    ("🔥", "CARDIO ZONE", "Treadmills, bikes, and ellipticals to torch calories and boost endurance."),
    ("🥊", "COMBAT FITNESS", "Boxing bags and combat training to build endurance, agility, and power."),
    ("👤", "PERSONAL TRAINING", "One-on-one sessions with certified trainers tailored to your goals."),
    ("🍎", "NUTRITION GUIDANCE", "Personalized diet plans and nutritional advice for your transformation."),
    ("⚡", "HIIT CLASSES", "High-Intensity Interval Training that maximizes fat burn in minimum time."),
    ("💪", "BODY BUILDING", "Dedicated programs for those looking to sculpt the perfect physique."),
    ("🧘", "FLEXIBILITY & CORE", "Stretching routines and core strengthening for performance and recovery."),
    ("📊", "BODY ASSESSMENT", "Regular body composition analysis and progress tracking on target."),
]
sg = '<div class="grid-auto">'
for icon, title, desc in services:
    sg += (
        '<div style="background:linear-gradient(135deg,#111,#1a1a1a);border:1px solid #1f2937;'
        'border-top:3px solid #dc2626;border-radius:10px;padding:28px 22px;text-align:center;">'
        f'<div style="font-size:2.5rem;margin-bottom:14px;">{icon}</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#fff;font-size:1.1rem;letter-spacing:2px;margin-bottom:10px;">{title}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.95rem;line-height:1.6;">{desc}</div>'
        '</div>'
    )
sg += '</div>'
st.markdown(sg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── STATS BANNER ────────────────────────────────────────────
st.markdown(
    '<div class="section-pad" style="background:linear-gradient(135deg,#7f1d1d,#991b1b,#7f1d1d);padding:60px 20px;">'
    '<div style="text-align:center;margin-bottom:30px;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(2rem,5vw,3.5rem);color:#fff;letter-spacing:4px;">OUR NUMBERS</div>'
    '</div>'
    '<div class="grid-4col">'
    '<div style="padding:30px 15px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
    '</div>'
    '<div style="padding:30px 15px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div style="padding:30px 15px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">50+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;">Equipment</div>'
    '</div>'
    '<div style="padding:30px 15px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">994</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
divider()

# ── PRICING ─────────────────────────────────────────────────
st.markdown('<div id="pricing" class="section-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("MEMBERSHIP", "PLANS", "INVEST IN YOUR BEST SELF")

def pricing_card(name, price, features, featured=False):
    bg = "linear-gradient(135deg,#1a0000,#2d0000)" if featured else "#111"
    border = "2px solid #dc2626" if featured else "1px solid #1f2937"
    shadow = "box-shadow:0 20px 60px rgba(220,38,38,0.3);" if featured else ""
    badge = ('<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);;'
             'background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;'
             'font-family:Oswald,sans-serif;font-size:0.7rem;letter-spacing:2px;'
             'padding:5px 18px;border-radius:0 0 8px 8px;white-space:nowrap;">MOST POPULAR</div>') if featured else ""
    mt = "margin-top:0px;" if not featured else ""
    feats = "".join([
        f'<div style="font-family:Rajdhani,sans-serif;color:#d1d5db;padding:8px 0;'
        f'border-bottom:1px solid {"#3f0000" if featured else "#1f2937"};font-size:0.95rem;">✅ {f}</div>'
        for f in features
    ])
    return (
        f'<div style="background:{bg};border:{border};border-radius:12px;padding:35px 24px;'
        f'text-align:center;{shadow}{mt}position:relative;">'
        f'{badge}'
        f'<div style="font-family:Bebas Neue,cursive;font-size:1.6rem;color:#fff;letter-spacing:3px;'
        f'margin-bottom:5px;{"margin-top:18px;" if featured else ""}">{name}</div>'
        f'<div style="font-family:Bebas Neue,cursive;font-size:3.5rem;color:#dc2626;line-height:1;margin:16px 0 4px;">'
        f'<span style="font-family:Oswald,sans-serif;font-size:1.3rem;color:#9ca3af;vertical-align:super;">Rs.</span>{price}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:2px;margin-bottom:22px;">PER MONTH</div>'
        f'<div style="text-align:left;margin-bottom:24px;">{feats}</div>'
        f'<a href="tel:9483834949" style="display:block;background:linear-gradient(135deg,#dc2626,#991b1b);'
        f'color:#fff;font-family:Oswald,sans-serif;font-size:0.9rem;letter-spacing:3px;'
        f'text-transform:uppercase;padding:13px;border-radius:6px;text-decoration:none;">📞 ENROLL NOW</a>'
        f'</div>'
    )

pg = '<div class="pricing-grid">'
pg += pricing_card("🥉 STARTER", "599",
    ["Gym Access — All Equipment", "Locker Room Access", "Basic Fitness Assessment", "Group Workout Sessions", "Cardio Zone Access"])
pg += pricing_card("🥇 ULTIMATE", "999",
    ["Everything in Starter", "Personal Training (4 Sessions)", "Nutrition Consultation", "Body Composition Analysis", "Progress Tracking", "Custom Diet Plan"],
    featured=True)
pg += pricing_card("🏆 CHAMPION", "1499",
    ["Everything in Ultimate", "Unlimited Personal Training", "Custom Workout Programs", "Advanced Nutrition Plan", "Monthly Body Analysis", "Competition Prep", "24/7 WhatsApp Support"])
pg += '</div>'
pg += ('<div style="text-align:center;margin-top:30px;">'
       '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
       'border-radius:8px;padding:12px 22px;max-width:90%;word-wrap:break-word;">'
       '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.85rem;letter-spacing:2px;">'
       'QUARTERLY &amp; ANNUAL DISCOUNTS AVAILABLE — CALL 9483834949'
       '</span></div></div>')
st.markdown(pg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── SCHEDULE ────────────────────────────────────────────────
st.markdown('<div id="schedule" class="section-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("GYM", "SCHEDULE", "WE'RE OPEN WHEN YOU NEED US")

days = [
    ("MONDAY",    "5:30AM–10AM", "4PM–9:30PM", "✅ OPEN",    "#10b981", "#111"),
    ("TUESDAY",   "5:30AM–10AM", "4PM–9:30PM", "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("WEDNESDAY", "5:30AM–10AM", "4PM–9:30PM", "✅ OPEN",    "#10b981", "#111"),
    ("THURSDAY",  "5:30AM–10AM", "4PM–9:30PM", "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("FRIDAY",    "5:30AM–10AM", "4PM–9:30PM", "✅ OPEN",    "#10b981", "#111"),
    ("SATURDAY",  "5:30AM–11AM", "4PM–8PM",    "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("SUNDAY",    "6AM–10AM",    "Closed",      "⚡ LIMITED", "#fbbf24", "#111"),
]

sch = '<div style="max-width:850px;margin:0 auto;border-radius:12px;overflow:hidden;border:1px solid #1f2937;overflow-x:auto;">'
sch += (
    '<div class="sched-row sched-header" style="display:grid;grid-template-columns:1.5fr 1.5fr 1.5fr 1fr;">'
    '<div style="padding:14px 16px;font-family:Oswald,sans-serif;color:#fff;font-size:0.85rem;letter-spacing:2px;">DAY</div>'
    '<div style="padding:14px 16px;font-family:Oswald,sans-serif;color:#fff;font-size:0.85rem;letter-spacing:2px;">MORNING</div>'
    '<div class="sched-head-eve" style="padding:14px 16px;font-family:Oswald,sans-serif;color:#fff;font-size:0.85rem;letter-spacing:2px;">EVENING</div>'
    '<div style="padding:14px 16px;font-family:Oswald,sans-serif;color:#fff;font-size:0.85rem;letter-spacing:2px;">STATUS</div>'
    '</div>'
)
for day, morning, evening, status, sc_col, bg in days:
    dc = "#dc2626" if "OPEN" in status else "#6b7280"
    sch += (
        f'<div class="sched-row" style="display:grid;grid-template-columns:1.5fr 1.5fr 1.5fr 1fr;background:{bg};border-bottom:1px solid #1f2937;">'
        f'<div style="padding:13px 16px;font-family:Oswald,sans-serif;color:{dc};font-size:0.85rem;letter-spacing:1px;">{day}</div>'
        f'<div style="padding:13px 16px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.9rem;">{morning}</div>'
        f'<div class="sched-cell-eve" style="padding:13px 16px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.9rem;">{evening}</div>'
        f'<div style="padding:13px 16px;font-family:Rajdhani,sans-serif;color:{sc_col};font-size:0.85rem;">{status}</div>'
        f'</div>'
    )
sch += '</div>'
sch += ('<div style="text-align:center;margin-top:22px;">'
        '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
        'border-radius:8px;padding:11px 20px;max-width:90%;word-wrap:break-word;">'
        '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:2px;">'
        'HOLIDAY HOURS MAY VARY — CALL 9483834949'
        '</span></div></div>')
st.markdown(sch, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── TESTIMONIALS ────────────────────────────────────────────
st.markdown('<div class="section-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("MEMBER", "STORIES", "REAL PEOPLE. REAL RESULTS.")
testimonials = [
    ("Sameer's Gym changed my life. In just 6 months, I lost 15kg and gained incredible strength. The trainers are amazing!", "RAHUL K.", "2021"),
    ("Best gym in Karwar! The atmosphere is electric. You walk in tired and walk out unstoppable. Sameer sir checks your form personally!", "PRIYA S.", "2022"),
    ("Nutrition guidance alone was worth the fee. I went from 65kg to lean 72kg in 8 months. Pure muscle gains!", "VISHAL D.", "2019"),
    ("As a woman, I was nervous. But the environment is so welcoming and professional. Trainers are respectful and knowledgeable!", "SNEHA R.", "2023"),
    ("Nothing compares to Sameer's. Personal training is exceptional. My transformation in 3 months was unbelievable!", "AKASH M.", "2020"),
    ("5:30 AM sessions are my favorite! Clean gym, pumping music, and amazing community spirit. Best decision ever!", "ADITYA N.", "2022"),
]
tg = '<div class="grid-auto">'
for text, author, year in testimonials:
    tg += (
        '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:26px;border-top:3px solid #dc2626;">'
        '<div style="color:#fbbf24;font-size:1rem;margin-bottom:8px;">★★★★★</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:1rem;line-height:1.7;margin-bottom:16px;font-style:italic;">"{text}"</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.85rem;letter-spacing:2px;">— {author}, since {year}</div>'
        '</div>'
    )
tg += '</div>'
st.markdown(tg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── CONTACT ─────────────────────────────────────────────────
st.markdown('<div id="contact" class="section-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("FIND &amp;", "CONNECT", "WE'D LOVE TO HEAR FROM YOU")
st.markdown(
    '<div class="grid-contact">'

    '<a href="tel:9483834949" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:26px 16px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2rem;margin-bottom:10px;">📞</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.7rem;letter-spacing:3px;margin-bottom:6px;">CALL / WHATSAPP</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.5rem;letter-spacing:2px;">9483834949</div>'
    '</div>'
    '</a>'

    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:26px 16px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2rem;margin-bottom:10px;">📸</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.7rem;letter-spacing:3px;margin-bottom:6px;">INSTAGRAM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.9rem;">@sameers_ultimatefitness</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.8rem;margin-top:4px;">994 Followers</div>'
    '</div>'
    '</a>'

    '<a href="https://maps.google.com/?q=Kodibaga+Main+Road+Karwar+Karnataka+581301" target="_blank" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:26px 16px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2rem;margin-bottom:10px;">📍</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.7rem;letter-spacing:3px;margin-bottom:6px;">LOCATION</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.85rem;line-height:1.5;">Kodibaga Main Road,<br>Karwar, Karnataka 581301</div>'
    '</div>'
    '</a>'

    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:26px 16px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2rem;margin-bottom:10px;">⏰</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.7rem;letter-spacing:3px;margin-bottom:6px;">HOURS</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.85rem;line-height:1.5;">Mon–Sat: 5:30AM–9:30PM<br>Sunday: 6AM–10AM</div>'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="max-width:900px;margin:0 auto;border-radius:12px;overflow:hidden;'
    'border:2px solid #dc2626;box-shadow:0 10px 40px rgba(220,38,38,0.2);">'
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3863.87!2d74.1279!3d14.8002!'
    '2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bbe8f6d0dffffff%3A0x1!'
    '2sKodibaga%20Main%20Rd%2C%20Karwar%2C%20Karnataka%20581301!5e0!3m2!1sen!2sin!4v1700000000000" '
    'width="100%" height="300" style="border:0;display:block;" allowfullscreen="" loading="lazy"></iframe>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ── CONTACT FORM ────────────────────────────────────────────
st.markdown('<div class="section-pad" style="background:#000;padding:60px 20px 20px;">', unsafe_allow_html=True)
section_header("START YOUR", "JOURNEY", "FILL THE FORM — WE'LL CALL YOU BACK")

col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    with st.form("join_form", clear_on_submit=True):
        name = st.text_input("YOUR FULL NAME *")
        phone = st.text_input("MOBILE NUMBER *")
        goal = st.selectbox("YOUR FITNESS GOAL", [
            "🏋️ Build Muscle & Strength",
            "🔥 Weight Loss & Fat Burning",
            "💪 Full Body Transformation",
            "🏃 Improve Stamina & Endurance",
            "🏆 Competition Preparation",
            "🧘 General Fitness & Wellness",
        ])
        plan = st.selectbox("PREFERRED PLAN", [
            "🥉 Starter Plan — Rs.599/month",
            "🥇 Ultimate Plan — Rs.999/month",
            "🏆 Champion Plan — Rs.1499/month",
            "📅 Quarterly Plan",
            "📅 Annual Plan",
            "❓ Not sure — Please advise",
        ])
        msg = st.text_area("MESSAGE (OPTIONAL)", height=90, placeholder="Tell us about your fitness goals...")
        submitted = st.form_submit_button("💪 SEND — LET'S GET STARTED!")
        if submitted:
            if name.strip() and phone.strip():
                st.success(f"✅ Awesome {name.upper()}! We'll call you on {phone} within 24 hours. Get ready to transform! 💪")
                st.balloons()
            else:
                st.error("⚠️ Please enter your name and phone number.")

st.markdown('<div style="padding-bottom:50px;"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── CTA BANNER ──────────────────────────────────────────────
st.markdown(
    '<div style="background:linear-gradient(135deg,#1a0000,#dc2626,#1a0000);padding:60px 20px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(1.8rem,7vw,5rem);'
    'color:#fff;letter-spacing:3px;text-shadow:0 4px 20px rgba(0,0,0,0.5);margin-bottom:10px;line-height:1.1;">'
    'YOUR TRANSFORMATION<br>STARTS TODAY'
    '</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:rgba(255,255,255,0.8);'
    'font-size:clamp(0.95rem,3vw,1.2rem);margin-bottom:30px;letter-spacing:1px;">'
    'Don\'t wait. Don\'t make excuses. <strong>START NOW.</strong>'
    '</div>'
    '<div class="cta-btns">'
    '<a href="tel:9483834949" style="display:inline-block;background:#fff;color:#dc2626;'
    'font-family:Oswald,sans-serif;font-size:1rem;font-weight:700;letter-spacing:3px;'
    'text-transform:uppercase;padding:16px 36px;border-radius:4px;text-decoration:none;'
    'box-shadow:0 8px 30px rgba(0,0,0,0.3);">📞 CALL: 9483834949</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" '
    'style="display:inline-block;background:transparent;color:#fff;'
    'font-family:Oswald,sans-serif;font-size:1rem;font-weight:700;letter-spacing:3px;'
    'text-transform:uppercase;padding:16px 36px;border-radius:4px;text-decoration:none;'
    'border:2px solid rgba(255,255,255,0.8);">📸 FOLLOW US</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# ── FOOTER ──────────────────────────────────────────────────
st.markdown(
    '<div style="background:#000;border-top:1px solid #111;padding:40px 20px 25px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2rem;color:#fff;letter-spacing:4px;margin-bottom:3px;">'
    'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span>'
    '</div>'
    '<div style="font-family:Oswald,sans-serif;font-size:0.8rem;color:#6b7280;letter-spacing:4px;margin-bottom:5px;">FITNESS &amp; GYM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.85rem;font-style:italic;margin-bottom:22px;">"A Place Where Champions Are Built" — Est. 2014</div>'

    '<div class="footer-links-row">'
    '<a href="#about" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.8rem;text-transform:uppercase;">About</a>'
    '<a href="#services" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.8rem;text-transform:uppercase;">Services</a>'
    '<a href="#pricing" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.8rem;text-transform:uppercase;">Pricing</a>'
    '<a href="#schedule" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.8rem;text-transform:uppercase;">Schedule</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.8rem;">Instagram</a>'
    '<a href="tel:9483834949" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.8rem;">Call Us</a>'
    '</div>'

    '<div class="footer-info-row">'
    '<span style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.9rem;">📞 9483834949</span>'
    '<span style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.9rem;">📍 Kodibaga Main Road, Karwar, KA 581301</span>'
    '</div>'

    '<div style="border-top:1px solid #111;padding-top:18px;font-family:Rajdhani,sans-serif;color:#374151;font-size:0.8rem;">'
    '© 2024 Sameer\'s Ultimate Fitness &amp; Gym. All Rights Reserved. Built with 💪 in Karwar'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)