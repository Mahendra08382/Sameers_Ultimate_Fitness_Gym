import streamlit as st
import base64
from pathlib import Path

# ── Helper to convert local image to base64 ──
@st.cache_data(show_spinner=False)
def get_image_base64(image_path):
    """Convert local image to base64 string for embedding in HTML"""
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        # Detect image type from extension
        ext = Path(image_path).suffix.lower().replace('.', '')
        if ext == 'jpg':
            ext = 'jpeg'
        return f"data:image/{ext};base64,{encoded}"
    except FileNotFoundError:
        return "" 

st.set_page_config(
    page_title="Sameer's Ultimate Fitness & Gym",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data(show_spinner=False)
def get_styles():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;600;700&family=Rajdhani:wght@400;500;600&display=swap');

#MainMenu {visibility:hidden;}
footer     {visibility:hidden;}
header     {visibility:hidden;}

.stApp { background:#0a0a0a !important; }

.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

* { box-sizing: border-box; }

/* ── FIXED NAV ── */
.fixed-nav {
    position: fixed !important;
    top: 0; left: 0; right: 0;
    width: 100%;
    z-index: 99999;
    background: rgba(0,0,0,0.98);
    border-bottom: 2px solid #dc2626;
    box-shadow: 0 4px 25px rgba(220,38,38,0.3);
}
.nav-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 13px 30px;
}
.nav-brand {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.5rem;
    color: #fff;
    letter-spacing: 3px;
    white-space: nowrap;
    cursor: default;
    user-select: none;
}
.nav-links {
    display: flex;
    gap: 22px;
    align-items: center;
}
.nav-links a {
    font-family: 'Oswald', sans-serif;
    color: #9ca3af;
    text-decoration: none;
    letter-spacing: 2px;
    font-size: 0.85rem;
    text-transform: uppercase;
    white-space: nowrap;
    transition: color 0.2s;
}
.nav-links a:hover  { color: #fff; }
.nav-links a.active { color: #dc2626 !important; font-weight: 700; }

/* ── MARQUEE ── */
.marquee-bar {
    background: linear-gradient(90deg,#dc2626,#991b1b,#dc2626);
    padding: 11px 0;
    overflow: hidden;
    white-space: nowrap;
}
.marquee-track {
    display: inline-block;
    animation: marquee 22s linear infinite;
    will-change: transform;
}

/* ── SPACER ── */
.nav-spacer {
    height: 88px;
    display: block;
}

/* ── SMOOTH SCROLL ── */
html { scroll-behavior: smooth; }
#home, #about, #services, #pricing, #schedule, #contact {
    scroll-margin-top: 90px;
}

/* ── DIVIDER ── */
.red-divider {
    height: 2px;
    background: linear-gradient(90deg,transparent,#dc2626,transparent);
    display: block;
}

/* ── ANIMATIONS ── */
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
@keyframes glow    { 0%{box-shadow:0 0 30px rgba(220,38,38,0.5)} 100%{box-shadow:0 0 70px rgba(220,38,38,0.9)} }
@keyframes slideUp { 0%{opacity:0;transform:translateY(20px)} 100%{opacity:1;transform:translateY(0)} }

/* ── FORM STYLES ── */
.stButton > button {
    background: linear-gradient(135deg,#dc2626,#991b1b) !important;
    color: white !important;
    font-family: 'Oswald',sans-serif !important;
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
label { color: #9ca3af !important; font-family: 'Oswald',sans-serif !important; }
div[data-testid="stForm"] {
    background: #111 !important;
    border: 1px solid #1f2937 !important;
    border-top: 3px solid #dc2626 !important;
    border-radius: 10px !important;
    padding: 20px !important;
}


/* ── PRICING CARDS WITH IMAGES — FIXED SIZING ── */
.pricing-card-wrapper {
    display: flex;
    flex-direction: column;
    height: 100%;
    background: #111;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #1f2937;
    transition: all 0.3s ease;
}

.pricing-card-wrapper:hover {
    transform: translateY(-8px);
    border-color: #dc2626;
    box-shadow: 0 15px 40px rgba(220,38,38,0.2);
}

.pricing-image {
    width: 100%;
    height: auto;           /* ← KEY FIX: let image keep its natural aspect ratio */
    object-fit: contain;    /* ← KEY FIX: show full image, no cropping */
    display: block;
    background: #0a0a0a;
}

.pricing-content {
    padding: 20px;
    display: flex;
    justify-content: center;
}

.pricing-btn {
    display: block;
    width: 100%;
    background: linear-gradient(135deg,#dc2626,#991b1b) !important;
    color: #fff !important;
    font-family: Oswald, sans-serif !important;
    font-size: 0.95rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    padding: 14px 16px !important;
    border-radius: 6px !important;
    text-decoration: none !important;
    text-align: center !important;
    transition: all 0.3s ease !important;
    border: none !important;
}

.pricing-btn:hover {
    box-shadow: 0 8px 20px rgba(220,38,38,0.4) !important;
    transform: scale(1.02);
}

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    max-width: 1300px;  /* ← increased from 1150px to fit 4 cards comfortably */
    margin: 0 auto;
    align-items: stretch;
}

/* ── MOBILE ── */
@media (max-width: 768px) {
    .nav-inner  { padding: 10px 12px; }
    .nav-brand  { font-size: 1.1rem; letter-spacing: 1px; }
    .nav-links  { gap: 10px; }
    .nav-links a { font-size: 0.6rem; letter-spacing: 1px; }
    .nav-spacer { height: 78px; }

    .hero-badge      { font-size: 0.58rem !important; padding: 5px 10px !important; }
    .logo-circle     { width: 115px !important; height: 115px !important; }
    .hero-t1         { font-size: 2.6rem !important; }
    .hero-t2         { font-size: 3.2rem !important; }
    .hero-tagline    { font-size: 0.88rem !important; }
    .hero-btn        { font-size: 0.7rem !important; padding: 10px 16px !important; letter-spacing: 1px !important; }
    .stat-num        { font-size: 1.8rem !important; }
    .stat-lbl        { font-size: 0.52rem !important; }
    .stat-col        { padding: 8px 12px !important; }

    .sec-title  { font-size: 2.2rem !important; }
    .sec-sub    { font-size: 0.65rem !important; }
    .sec-wrap   { padding: 50px 14px !important; }

    .pricing-grid   { grid-template-columns: 1fr !important; }
    .pricing-name   { font-size: 1.1rem !important; }
    .pricing-price  { font-size: 2.2rem !important; }

    .sched-hd   { padding: 10px 6px !important; font-size: 0.6rem !important; }
    .sched-day  { font-size: 0.6rem !important; padding: 10px 6px !important; }

    .test-card  { padding: 18px 14px !important; }
    .cta-t      { font-size: 1.8rem !important; }
    .ft-brand   { font-size: 1.5rem !important; }
}

@media (max-width: 600px) {
    .pricing-grid { grid-template-columns: 1fr !important; }
    .pricing-image { height: 150px !important; }
    .pricing-price { font-size: 2rem !important; }
}
</style>
"""

st.markdown(get_styles(), unsafe_allow_html=True)

# ── helpers ─────────────────────────────────────────────────
def divider():
    st.markdown(
        '<div class="red-divider"></div>',
        unsafe_allow_html=True
    )

def section_header(title, highlight, subtitle):
    st.markdown(
        '<div style="text-align:center;margin-bottom:40px;">'
        f'<div class="sec-title" style="font-family:Bebas Neue,cursive;'
        f'font-size:clamp(2.2rem,6vw,4.5rem);color:#fff;letter-spacing:4px;margin:0;line-height:1;">'
        f'{title} <span style="color:#dc2626;">{highlight}</span></div>'
        '<div style="width:70px;height:4px;background:linear-gradient(90deg,#dc2626,#991b1b);'
        'margin:12px auto 14px;border-radius:2px;"></div>'
        f'<div class="sec-sub" style="font-family:Oswald,sans-serif;color:#6b7280;'
        f'font-size:0.85rem;letter-spacing:3px;text-transform:uppercase;">{subtitle}</div>'
        '</div>',
        unsafe_allow_html=True
    )

@st.cache_data(show_spinner=False)
def marquee_inner():
    items = ["💪 TRAIN HARD","🔥 BURN STRONGER","⚡ NO EXCUSES",
             "🏆 CHAMPIONS BUILT HERE","💥 PUSH YOUR LIMITS","🎯 RESULTS GUARANTEED"]
    mi = ""
    for item in items * 2:
        mi += (f'<span style="font-family:Bebas Neue,cursive;font-size:1.1rem;'
               f'color:#fff;letter-spacing:3px;padding:0 20px;">{item}</span>'
               f'<span style="color:rgba(255,255,255,0.4);padding:0 4px;">•</span>')
    return mi


# ══════════════════════════════════════════════════════════════
# FIXED NAV + MARQUEE
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div class="fixed-nav">'
      '<div class="nav-inner">'
        '<span class="nav-brand">'
          'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span>'
        '</span>'
        '<div class="nav-links">'
          '<a href="#home">HOME</a>'
          '<a href="#about">ABOUT</a>'
          '<a href="#services">SERVICES</a>'
          '<a href="#pricing">PRICING</a>'
          '<a href="#schedule">SCHEDULE</a>'
          '<a href="#contact" class="active">JOIN NOW</a>'
        '</div>'
      '</div>'
      '<div class="marquee-bar">'
        f'<div class="marquee-track">{marquee_inner()}</div>'
      '</div>'
      '<div class="red-divider"></div>'
    '</div>'
    '<div class="nav-spacer"></div>',
    unsafe_allow_html=True
)

# ══════════════════════════════════════════════════════════════
# HERO SECTION
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div id="home" class="sec-wrap" style="'
    'background:radial-gradient(ellipse at top,#1a0000 0%,#000 50%,#050505 100%);'
    'min-height:90vh;display:flex;flex-direction:column;align-items:center;'
    'justify-content:center;text-align:center;padding:60px 16px 50px;">'

    '<div class="hero-badge" style="background:linear-gradient(90deg,#dc2626,#991b1b);'
    'color:#fff;font-family:Oswald,sans-serif;font-size:0.75rem;letter-spacing:3px;'
    'text-transform:uppercase;padding:7px 18px;border-radius:2px;margin-bottom:24px;'
    'white-space:nowrap;">EST. 2014 — KARWAR\'S #1 FITNESS DESTINATION</div>'

    '<div class="logo-circle" style="width:155px;height:155px;border-radius:50%;'
    'background:linear-gradient(135deg,#1a1a1a,#000);border:3px solid #dc2626;'
    'display:flex;align-items:center;justify-content:center;margin:0 auto 26px;'
    'animation:glow 2s ease-in-out infinite alternate;will-change:box-shadow;">'
      '<div style="text-align:center;padding:10px;">'
        '<div style="font-size:1.9rem;">🏋️</div>'
        '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1rem;'
        'letter-spacing:2px;line-height:1.15;">SAMEER\'S</div>'
        '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.25rem;'
        'letter-spacing:2px;line-height:1.1;">ULTIMATE</div>'
        '<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.45rem;'
        'letter-spacing:1px;">FITNESS &amp; GYM</div>'
      '</div>'
    '</div>'

    '<div class="hero-t1" style="font-family:Bebas Neue,cursive;'
    'font-size:clamp(3rem,10vw,8rem);color:#fff;line-height:0.9;letter-spacing:4px;'
    'text-shadow:0 0 40px rgba(220,38,38,0.4);">FORGE YOUR</div>'

    '<div class="hero-t2" style="font-family:Bebas Neue,cursive;'
    'font-size:clamp(3.5rem,13vw,10rem);color:#dc2626;line-height:0.9;letter-spacing:4px;'
    'text-shadow:0 0 60px rgba(220,38,38,0.7);margin-bottom:16px;">GREATNESS</div>'

    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;'
    'font-size:clamp(0.65rem,2vw,1rem);letter-spacing:4px;text-transform:uppercase;'
    'margin-bottom:10px;">FITNESS &amp; GYM • KARWAR, KARNATAKA</div>'

    '<div class="hero-tagline" style="font-family:Rajdhani,sans-serif;color:#f3f4f6;'
    'font-size:clamp(0.9rem,3vw,1.4rem);font-style:italic;margin-bottom:30px;">'
      '<span style="color:#dc2626;font-size:1.8rem;">"</span>'
      'A place where champions are built'
      '<span style="color:#dc2626;font-size:1.8rem;">"</span>'
    '</div>'

    '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:45px;">'
      '<a class="hero-btn" href="tel:9483834949" style="background:linear-gradient(135deg,#dc2626,#991b1b);'
      'color:#fff;font-family:Oswald,sans-serif;font-size:0.95rem;letter-spacing:2px;'
      'text-transform:uppercase;padding:14px 28px;border-radius:4px;text-decoration:none;'
      'border:2px solid #dc2626;white-space:nowrap;">📞 JOIN — 9483834949</a>'
      '<a class="hero-btn" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" '
      'style="background:transparent;color:#fff;font-family:Oswald,sans-serif;font-size:0.95rem;'
      'letter-spacing:2px;text-transform:uppercase;padding:14px 28px;border-radius:4px;'
      'text-decoration:none;border:2px solid #fff;white-space:nowrap;">📸 FOLLOW US</a>'
    '</div>'

    '<div style="display:flex;justify-content:center;">'
      '<div class="stat-col" style="text-align:center;padding:10px 22px;border-right:1px solid #374151;">'
        '<div class="stat-num" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">10+</div>'
        '<div class="stat-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
      '</div>'
      '<div class="stat-col" style="text-align:center;padding:10px 22px;border-right:1px solid #374151;">'
        '<div class="stat-num" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">100+</div>'
        '<div class="stat-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
      '</div>'
      '<div class="stat-col" style="text-align:center;padding:10px 22px;border-right:1px solid #374151;">'
        '<div class="stat-num" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">1k +</div>'
        '<div class="stat-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
      '</div>'
      '<div class="stat-col" style="text-align:center;padding:10px 22px;">'
        '<div class="stat-num" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">100%</div>'
        '<div class="stat-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Dedication</div>'
      '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
divider()

# ══════════════════════════════════════════════════════════════
# ABOUT SECTION
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div id="about" class="sec-wrap" style="background:#050505;padding:75px 30px;">',
    unsafe_allow_html=True
)
section_header("ABOUT","US","BUILDING CHAMPIONS SINCE 2014")
st.markdown(
    '<div class="about-flex" style="display:flex;gap:50px;align-items:center;'
    'flex-wrap:wrap;max-width:1000px;margin:0 auto;">'

      '<div style="flex:1;min-width:260px;">'
        '<p class="about-text-p" style="font-family:Rajdhani,sans-serif;color:#9ca3af;'
        'font-size:1.05rem;line-height:1.9;margin-bottom:18px;">'
        'Welcome to <strong style="color:#dc2626;">Sameer\'s Ultimate Fitness &amp; Gym</strong> '
        '— Karwar\'s premier fitness destination, established in 2014. For over a decade, '
        'we\'ve been transforming lives, building champions, and creating a community of unstoppable athletes.'
        '</p>'
        '<p class="about-text-p" style="font-family:Rajdhani,sans-serif;color:#9ca3af;'
        'font-size:1.05rem;line-height:1.9;margin-bottom:24px;">'
        'Located on <strong style="color:#fff;">Green street Road, Karwar</strong>, we offer '
        'state-of-the-art equipment, expert trainers, and an electrifying atmosphere that pushes '
        'you beyond limits every day.'
        '</p>'
        '<div style="display:flex;gap:10px;flex-wrap:wrap;">'
          '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);'
          'border-radius:6px;padding:10px 18px;text-align:center;">'
            '<div class="about-mini-val" style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">12+</div>'
            '<div class="about-mini-lbl" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">YEARS</div>'
          '</div>'
          '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);'
          'border-radius:6px;padding:10px 18px;text-align:center;">'
            '<div class="about-mini-val" style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">100+</div>'
            '<div class="about-mini-lbl" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">MEMBERS</div>'
          '</div>'
          '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);'
          'border-radius:6px;padding:10px 18px;text-align:center;">'
            '<div class="about-mini-val" style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">100%</div>'
            '<div class="about-mini-lbl" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">RESULTS</div>'
          '</div>'
        '</div>'
      '</div>'

      '<div class="about-visual" style="flex:0 0 250px;min-width:220px;">'
        '<div style="background:linear-gradient(135deg,#1a0000,#2d0000);border:2px solid #dc2626;'
        'border-radius:12px;padding:40px 22px;text-align:center;'
        'box-shadow:0 20px 60px rgba(220,38,38,0.25);">'
          '<div style="font-size:3.2rem;margin-bottom:12px;">🏋️</div>'
          '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.5rem;letter-spacing:4px;">SAMEER\'S</div>'
          '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:2.2rem;letter-spacing:4px;line-height:1;">ULTIMATE</div>'
          '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);margin:10px 0;"></div>'
          '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:3px;">FITNESS &amp; GYM</div>'
          '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.65rem;letter-spacing:2px;margin-top:4px;">EST 2014</div>'
        '</div>'
      '</div>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# WHY CHOOSE US
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap" style="background:#000;padding:75px 30px;">', unsafe_allow_html=True)
section_header("WHY","CHOOSE US","WHAT MAKES US KARWAR'S BEST GYM")
why_items = [
    ("🏆","PROVEN RESULTS",     "Hundreds of success stories from real members who transformed their bodies."),
    ("💡","EXPERT COACHING",    "Certified trainers with years of experience guiding you every step."),
    ("⚙️","MODERN EQUIPMENT",  "State-of-the-art machines and free weights for the ultimate workout."),
    ("🔥","INTENSE ATMOSPHERE", "An electrifying environment that keeps you motivated every day."),
    ("👥","STRONG COMMUNITY",   "A brotherhood of fitness enthusiasts pushing each other to excel."),
    ("📍","PRIME LOCATION",     "Conveniently located on Green Street Road, Karwar."),
]
wg = '<div class="why-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:1100px;margin:0 auto;">'
for ic,ti,de in why_items:
    wg += (
        '<div class="why-card" style="background:rgba(220,38,38,0.05);border:1px solid rgba(220,38,38,0.2);'
        'border-radius:10px;padding:24px 16px;text-align:center;">'
        f'<div class="why-icon" style="font-size:2rem;margin-bottom:10px;">{ic}</div>'
        f'<div class="why-ttl"  style="font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;margin-bottom:7px;">{ti}</div>'
        f'<div class="why-dsc"  style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.85rem;line-height:1.5;">{de}</div>'
        '</div>'
    )
wg += '</div>'
st.markdown(wg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# SERVICES
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="services" class="sec-wrap" style="background:#050505;padding:75px 30px;">', unsafe_allow_html=True)
section_header("OUR","SERVICES","EVERYTHING YOU NEED TO REACH YOUR PEAK")
services = [
    ("🏋️","WEIGHT TRAINING",   "Comprehensive strength training with free weights, barbells, and machines."),
    ("🔥","CARDIO ZONE",        "Treadmills, bikes, and ellipticals to torch calories and boost endurance."),
    ("🥊","COMBAT FITNESS",     "Boxing bags and combat training to build endurance, agility, and power."),
    ("👤","PERSONAL TRAINING",  "One-on-one sessions with certified trainers tailored to your goals."),
    ("🍎","NUTRITION GUIDANCE", "Personalized diet plans and nutritional advice for your transformation."),
    ("⚡","HIIT CLASSES",       "High-Intensity Interval Training that maximizes fat burn in minimum time."),
    ("💪","BODY BUILDING",      "Dedicated programs for those looking to sculpt the perfect physique."),
    ("🧘","FLEXIBILITY & CORE", "Stretching routines and core strengthening for performance and recovery."),
    ("📊","BODY ASSESSMENT",    "Regular body composition analysis and progress tracking to stay on target."),
]
sg = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;max-width:1150px;margin:0 auto;">'
for ic,ti,de in services:
    sg += (
        '<div class="svc-card" style="background:linear-gradient(135deg,#111,#1a1a1a);border:1px solid #1f2937;'
        'border-top:3px solid #dc2626;border-radius:10px;padding:26px 20px;text-align:center;">'
        f'<div class="svc-icon" style="font-size:2.2rem;margin-bottom:12px;">{ic}</div>'
        f'<div class="svc-ttl"  style="font-family:Oswald,sans-serif;color:#fff;font-size:1rem;letter-spacing:2px;margin-bottom:9px;">{ti}</div>'
        f'<div class="svc-dsc"  style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;line-height:1.55;">{de}</div>'
        '</div>'
    )
sg += '</div>'
st.markdown(sg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# STATS BANNER
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div class="sec-wrap" style="background:linear-gradient(135deg,#7f1d1d,#991b1b,#7f1d1d);padding:60px 30px;">'
    '<div style="text-align:center;margin-bottom:28px;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(1.8rem,5vw,3.5rem);color:#fff;letter-spacing:4px;">OUR NUMBERS</div>'
    '</div>'
    '<div style="display:grid;grid-template-columns:repeat(4,1fr);max-width:900px;margin:0 auto;'
    'background:#0a0a0a;border-radius:12px;overflow:hidden;border:1px solid #1f2937;">'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val" style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">12+</div>'
    '<div class="num-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val" style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">100+</div>'
    '<div class="num-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val" style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">50+</div>'
    '<div class="num-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Equipment</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;">'
    '<div class="num-val" style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">1K +</div>'
    '<div class="num-lbl" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
divider()

# ══════════════════════════════════════════════════════════════
# PRICING WITH IMAGES
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="pricing" class="sec-wrap" style="background:#000;padding:75px 30px;">', unsafe_allow_html=True)
section_header("MEMBERSHIP","PLANS","INVEST IN YOUR BEST SELF")

# Just image paths - no need for name/price/features since image has it all
pricing_images = [
    "images/Price1.jpeg",
    "images/Price2.jpeg",
    "images/Price3.jpeg",
    "images/Price4.jpeg",

]

# Generate pricing HTML — image + button only
pricing_html = '<div class="pricing-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;max-width:1300px;margin:0 auto;align-items:stretch;">'

for image_path in pricing_images:
    img_data = get_image_base64(image_path)
    img_tag = f'<img src="{img_data}" alt="Pricing Plan" class="pricing-image">' if img_data else '<div style="padding:40px;text-align:center;color:#6b7280;">Image not found</div>'
    
    card_html = (
        f'<div class="pricing-card-wrapper">'
        f'{img_tag}'
        f'<div class="pricing-content">'
        f'<a href="tel:9483834949" class="pricing-btn">📞 ENROLL NOW</a>'
        f'</div>'
        f'</div>'
    )
    pricing_html += card_html

pricing_html += '</div>'

st.markdown(pricing_html, unsafe_allow_html=True)

# Discount banner
st.markdown(
    '<div style="text-align:center;margin-top:40px;">'
    '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
    'border-radius:8px;padding:14px 24px;max-width:95%;">'
    '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.85rem;letter-spacing:2px;">'
    '⏰ QUARTERLY &amp; ANNUAL DISCOUNTS AVAILABLE — CALL 9483834949'
    '</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# SCHEDULE
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="schedule" class="sec-wrap" style="background:#050505;padding:75px 30px;">', unsafe_allow_html=True)
section_header("GYM","SCHEDULE","WE'RE OPEN WHEN YOU NEED US")

@st.cache_data(show_spinner=False)
def get_schedule_html():
    days = [
        ("MONDAY",   "5:30AM–10AM","4PM–9:30PM","✅ OPEN",   "#10b981","#111"),
        ("TUESDAY",  "5:30AM–10AM","4PM–9:30PM","✅ OPEN",   "#10b981","#0a0a0a"),
        ("WEDNESDAY","5:30AM–10AM","4PM–9:30PM","✅ OPEN",   "#10b981","#111"),
        ("THURSDAY", "5:30AM–10AM","4PM–9:30PM","✅ OPEN",   "#10b981","#0a0a0a"),
        ("FRIDAY",   "5:30AM–10AM","4PM–9:30PM","✅ OPEN",   "#10b981","#111"),
        ("SATURDAY", "5:30AM–11AM","4PM–8PM",   "✅ OPEN",   "#10b981","#0a0a0a"),
        ("SUNDAY",   "6AM–10AM",   "Closed",    "⚡ LIMITED","#fbbf24","#111"),
    ]
    s = ('<div style="max-width:850px;margin:0 auto;border-radius:12px;overflow:hidden;'
         'border:1px solid #1f2937;overflow-x:auto;">'
         '<table style="width:100%;border-collapse:collapse;min-width:320px;">'
         '<thead><tr style="background:linear-gradient(135deg,#dc2626,#991b1b);">'
         '<th class="sched-hd" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">DAY</th>'
         '<th class="sched-hd" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">MORNING</th>'
         '<th class="sched-hd" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">EVENING</th>'
         '<th class="sched-hd" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">STATUS</th>'
         '</tr></thead><tbody>')
    for day,mo,ev,st_,sc,bg in days:
        dc = "#dc2626" if "OPEN" in st_ else "#6b7280"
        s += (f'<tr style="background:{bg};border-bottom:1px solid #1f2937;">'
              f'<td class="sched-day"  style="padding:12px 14px;font-family:Oswald,sans-serif;color:{dc};font-size:0.82rem;letter-spacing:1px;">{day}</td>'
              f'<td class="sched-time" style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.85rem;">{mo}</td>'
              f'<td class="sched-time" style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.85rem;">{ev}</td>'
              f'<td class="sched-st"   style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:{sc};font-size:0.82rem;">{st_}</td>'
              '</tr>')
    s += ('</tbody></table></div>'
          '<div style="text-align:center;margin-top:20px;">'
          '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
          'border-radius:8px;padding:11px 18px;max-width:95%;">'
          '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.78rem;letter-spacing:2px;">'
          'HOLIDAY HOURS MAY VARY — CALL 9483834949</span></div></div>')
    return s

st.markdown(get_schedule_html(), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# TESTIMONIALS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap" style="background:#000;padding:75px 30px;">', unsafe_allow_html=True)
section_header("MEMBER","STORIES","REAL PEOPLE. REAL RESULTS.")

@st.cache_data(show_spinner=False)
def get_testimonials_html():
    data = [
        ("Sameer's Gym changed my life. In 6 months I lost 15kg and gained incredible strength!","RAHUL K.","2021"),
        ("Best gym in Karwar! Electric atmosphere. Walk in tired, walk out unstoppable!","PRIYA S.","2022"),
        ("Nutrition guidance alone was worth the fee. From 65kg to lean 72kg in 8 months!","VISHAL D.","2019"),
        ("As a woman I was nervous. Environment is so welcoming. Trainers are amazing!","SNEHA R.","2023"),
        ("Nothing compares to Sameer's. Transformation in 3 months was unbelievable!","AKASH M.","2020"),
        ("5:30 AM sessions are my favorite! Clean gym, pumping music, amazing community!","ADITYA N.","2022"),
    ]
    tg = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;max-width:1100px;margin:0 auto;">'
    for tx,au,yr in data:
        tg += (
            '<div class="test-card" style="background:#111;border:1px solid #1f2937;border-radius:10px;'
            'padding:24px;border-top:3px solid #dc2626;">'
            f'<div class="test-star" style="color:#fbbf24;font-size:1rem;margin-bottom:8px;">★★★★★</div>'
            f'<div class="test-txt"  style="font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.95rem;line-height:1.65;margin-bottom:14px;font-style:italic;">"{tx}"</div>'
            f'<div class="test-auth" style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.82rem;letter-spacing:2px;">— {au}, since {yr}</div>'
            '</div>'
        )
    tg += '</div>'
    return tg

st.markdown(get_testimonials_html(), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="contact" class="sec-wrap" style="background:#050505;padding:75px 30px;">', unsafe_allow_html=True)
section_header("FIND &amp;","CONNECT","WE'D LOVE TO HEAR FROM YOU")

cards = [
    ("📞", "CALL / WHATSAPP", "9483834949", "tel:9483834949"),
    ("📸", "INSTAGRAM", "@sameers_ultimatefitness<br><span style='font-size:0.75rem;color:#6b7280;'>1000+ Followers</span>", "https://www.instagram.com/sameers_ultimatefitness/"),
    ("📍", "LOCATION", "Green Street Road,<br>Karwar, Karnataka 581301", "https://www.google.com/maps/search/?api=1&query=Sameer%27s%20Ultimate%20Fitness%20%26%20Gym%2C%20Karwar"),
    ("⏰", "HOURS", "Mon–Sat: 5:30AM–9:30PM<br>Sunday: 6AM–10AM", None),
]

cg = '<div class="crd-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:1000px;margin:0 auto 45px;">'
for ic,lb,vl,lk in cards:
    inner = (
        f'<div class="crd-card" style="background:#111;border:1px solid #1f2937;border-radius:10px;'
        f'padding:24px 12px;text-align:center;border-top:3px solid #dc2626;">'
        f'<div class="crd-icon" style="font-size:1.8rem;margin-bottom:9px;">{ic}</div>'
        f'<div class="crd-lbl"  style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">{lb}</div>'
        f'<div class="crd-val"  style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.85rem;line-height:1.5;">{vl}</div>'
        f'</div>'
    )
    cg += f'<a href="{lk}" target="_blank" style="text-decoration:none;">{inner}</a>' if lk else inner
cg += '</div>'
st.markdown(cg, unsafe_allow_html=True)

st.markdown(
    '<div style="max-width:900px;margin:0 auto;border-radius:12px;overflow:hidden;border:2px solid #dc2626;box-shadow:0 10px 40px rgba(220,38,38,0.2);">'
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3857.2664353260902!2d74.12675567371929!3d14.810297385701233!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bbe611b4a2f1e83%3A0x47c6ec0f3b613028!2sSameer\'s%20Ultimate%20Fitness%20%26%20Gym!5e0!3m2!1sen!2sin!4v1791888489396!5m2!1sen!2sin" '
    'width="100%" '
    'height="350" '
    'style="border:0;display:block;" '
    'allowfullscreen="" '
    'loading="lazy" '
    'referrerpolicy="strict-origin-when-cross-origin">'
    '</iframe>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

# ══════════════════════════════════════════════════════════════
# CONTACT FORM
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="sec-wrap" style="background:#000;padding:65px 30px 30px;">', unsafe_allow_html=True)
section_header("START YOUR","JOURNEY","FILL THE FORM — WE'LL CALL YOU BACK")

col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    with st.form("join_form", clear_on_submit=True):
        name  = st.text_input("YOUR FULL NAME *")
        phone = st.text_input("MOBILE NUMBER *")
        goal  = st.selectbox("YOUR FITNESS GOAL", [
            "🏋️ Build Muscle & Strength","🔥 Weight Loss & Fat Burning",
            "💪 Full Body Transformation","🏃 Improve Stamina & Endurance",
            "🏆 Competition Preparation","🧘 General Fitness & Wellness",
        ])
        plan = st.selectbox("PREFERRED PLAN", [
            "🥉 Starter Plan — Rs.599/month","🥇 Ultimate Plan — Rs.999/month",
            "🏆 Champion Plan — Rs.1499/month","📅 Quarterly Plan",
            "📅 Annual Plan","❓ Not sure — Please advise",
        ])
        msg  = st.text_area("MESSAGE (OPTIONAL)", height=90,
                            placeholder="Tell us about your fitness goals...")
        sub  = st.form_submit_button("💪 SEND — LET'S GET STARTED!")
        if sub:
            if name.strip() and phone.strip():
                st.success(f"✅ Awesome {name.upper()}! We'll call you on {phone} within 24 hours. Get ready to transform! 💪")
                st.balloons()
            else:
                st.error("⚠️ Please enter your name and phone number.")

st.markdown('<div style="padding-bottom:50px;"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# CTA BANNER
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div class="sec-wrap" style="background:linear-gradient(135deg,#1a0000,#dc2626,#1a0000);'
    'padding:65px 30px;text-align:center;">'
    '<div class="cta-t" style="font-family:Bebas Neue,cursive;font-size:clamp(1.8rem,7vw,5rem);'
    'color:#fff;letter-spacing:3px;text-shadow:0 4px 20px rgba(0,0,0,0.5);margin-bottom:10px;line-height:1.1;">'
    'YOUR TRANSFORMATION STARTS TODAY</div>'
    '<div class="cta-s" style="font-family:Rajdhani,sans-serif;color:rgba(255,255,255,0.85);'
    'font-size:clamp(0.9rem,3vw,1.2rem);margin-bottom:28px;">'
    'Don\'t wait. Don\'t make excuses. <strong>START NOW.</strong></div>'
    '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">'
    '<a class="cta-btn" href="tel:9483834949" style="display:inline-block;background:#fff;color:#dc2626;'
    'font-family:Oswald,sans-serif;font-size:1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;'
    'padding:15px 32px;border-radius:4px;text-decoration:none;white-space:nowrap;">📞 CALL: 9483834949</a>'
    '<a class="cta-btn" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" '
    'style="display:inline-block;background:transparent;color:#fff;font-family:Oswald,sans-serif;'
    'font-size:1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;'
    'padding:15px 32px;border-radius:4px;text-decoration:none;border:2px solid rgba(255,255,255,0.8);'
    'white-space:nowrap;">📸 FOLLOW US</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown(
    '<div class="sec-wrap" style="background:#000;border-top:1px solid #111;padding:45px 30px 28px;text-align:center;">'
    '<div class="ft-brand" style="font-family:Bebas Neue,cursive;font-size:2rem;color:#fff;letter-spacing:4px;margin-bottom:3px;">'
    'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span></div>'
    '<div style="font-family:Oswald,sans-serif;font-size:0.8rem;color:#6b7280;letter-spacing:4px;margin-bottom:4px;">FITNESS &amp; GYM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.85rem;font-style:italic;margin-bottom:20px;">"A Place Where Champions Are Built" — Est. 2014</div>'
    '<div style="display:flex;justify-content:center;gap:22px;flex-wrap:wrap;margin-bottom:18px;">'
    '<a class="ft-lnk" href="#home"     style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Home</a>'
    '<a class="ft-lnk" href="#about"    style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">About</a>'
    '<a class="ft-lnk" href="#services" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Services</a>'
    '<a class="ft-lnk" href="#pricing"  style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Pricing</a>'
    '<a class="ft-lnk" href="#schedule" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Schedule</a>'
    '<a class="ft-lnk" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.78rem;">Instagram</a>'
    '<a class="ft-lnk" href="tel:9483834949" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.78rem;">Call Us</a>'
    '</div>'
    '<div style="display:flex;justify-content:center;gap:22px;flex-wrap:wrap;margin-bottom:20px;">'
    '<span class="ft-inf" style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;">📞 9483834949</span>'
    '<span class="ft-inf" style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;">📍 Greenstreet Road, Karwar, KA 581301</span>'
    '</div>'
    '<div style="border-top:1px solid #111;padding-top:16px;">'
    '<span style="font-family:Rajdhani,sans-serif;color:#374151;font-size:0.78rem;">'
    '© 2024 Sameer\'s Ultimate Fitness &amp; Gym. All Rights Reserved. Built with 💪 in Karwar'
    '</span></div>'
    '</div>',
    unsafe_allow_html=True
)