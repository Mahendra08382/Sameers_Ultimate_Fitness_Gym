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

@media (max-width: 768px) {
    .nav-wrap { padding: 10px 12px !important; }
    .nav-brand-text { font-size: 1.1rem !important; letter-spacing: 1px !important; }
    .nav-link { font-size: 0.65rem !important; letter-spacing: 1px !important; }
    .nav-gap { gap: 10px !important; }
    .hero-badge { font-size: 0.6rem !important; letter-spacing: 2px !important; padding: 5px 12px !important; }
    .logo-circle { width: 110px !important; height: 110px !important; }
    .logo-gym-icon { font-size: 1.4rem !important; }
    .logo-name { font-size: 0.85rem !important; }
    .logo-ult { font-size: 1rem !important; }
    .logo-sub { font-size: 0.38rem !important; }
    .hero-title-main { font-size: 2.4rem !important; letter-spacing: 2px !important; }
    .hero-title-red { font-size: 3rem !important; letter-spacing: 2px !important; }
    .hero-tagline { font-size: 0.9rem !important; }
    .hero-tagline-quote { font-size: 1.2rem !important; }
    .hero-btn-primary, .hero-btn-secondary { font-size: 0.7rem !important; padding: 10px 16px !important; letter-spacing: 1px !important; }
    .stat-number { font-size: 1.8rem !important; }
    .stat-label { font-size: 0.55rem !important; letter-spacing: 1px !important; }
    .stat-divider { padding: 8px 10px !important; }
    .marquee-item { font-size: 0.85rem !important; padding: 0 12px !important; letter-spacing: 2px !important; }
    .sec-title { font-size: 2rem !important; letter-spacing: 2px !important; }
    .sec-sub { font-size: 0.65rem !important; letter-spacing: 2px !important; }
    .sec-pad { padding: 45px 12px !important; }
    .about-grid { gap: 20px !important; }
    .about-visual { padding: 30px 15px !important; }
    .about-visual-name { font-size: 1.2rem !important; }
    .about-visual-ult { font-size: 1.8rem !important; }
    .about-stat-val { font-size: 1.3rem !important; }
    .about-stat-label { font-size: 0.55rem !important; }
    .about-text-p { font-size: 0.8rem !important; line-height: 1.6 !important; }
    .about-stats-row { gap: 6px !important; }
    .about-stat-box { padding: 8px 10px !important; }
    .why-grid { gap: 8px !important; }
    .why-icon { font-size: 1.5rem !important; }
    .why-title { font-size: 0.7rem !important; letter-spacing: 1px !important; }
    .why-desc { font-size: 0.65rem !important; }
    .why-card { padding: 16px 10px !important; }
    .svc-icon { font-size: 1.8rem !important; }
    .svc-title { font-size: 0.8rem !important; letter-spacing: 1px !important; }
    .svc-desc { font-size: 0.75rem !important; }
    .svc-card { padding: 20px 14px !important; }
    .num-val { font-size: 2rem !important; }
    .num-label { font-size: 0.6rem !important; letter-spacing: 1px !important; }
    .num-cell { padding: 20px 8px !important; }
    .pricing-grid { gap: 8px !important; }
    .plan-name { font-size: 1rem !important; letter-spacing: 1px !important; }
    .plan-price { font-size: 2.2rem !important; }
    .plan-price-sym { font-size: 0.9rem !important; }
    .plan-period { font-size: 0.6rem !important; letter-spacing: 1px !important; }
    .plan-feat { font-size: 0.65rem !important; padding: 6px 0 !important; }
    .plan-btn { font-size: 0.65rem !important; letter-spacing: 1px !important; padding: 10px !important; }
    .plan-card { padding: 20px 12px !important; }
    .plan-badge { font-size: 0.55rem !important; padding: 4px 12px !important; }
    .sched-head-cell { padding: 10px 8px !important; font-size: 0.65rem !important; letter-spacing: 1px !important; }
    .sched-day { font-size: 0.65rem !important; padding: 10px 8px !important; letter-spacing: 0 !important; }
    .sched-time { font-size: 0.65rem !important; padding: 10px 6px !important; }
    .sched-status { font-size: 0.6rem !important; padding: 10px 6px !important; }
    .test-stars { font-size: 0.85rem !important; }
    .test-text { font-size: 0.8rem !important; line-height: 1.5 !important; }
    .test-author { font-size: 0.7rem !important; letter-spacing: 1px !important; }
    .test-card { padding: 18px 14px !important; }
    .contact-grid { gap: 8px !important; }
    .contact-icon { font-size: 1.5rem !important; }
    .contact-label { font-size: 0.55rem !important; letter-spacing: 1px !important; }
    .contact-val { font-size: 0.75rem !important; }
    .contact-card { padding: 18px 8px !important; }
    .cta-title { font-size: 1.8rem !important; letter-spacing: 2px !important; }
    .cta-sub { font-size: 0.85rem !important; }
    .cta-btn-w { font-size: 0.8rem !important; padding: 13px 22px !important; letter-spacing: 2px !important; }
    .cta-btn-t { font-size: 0.8rem !important; padding: 13px 22px !important; letter-spacing: 2px !important; }
    .footer-brand { font-size: 1.5rem !important; }
    .footer-sub { font-size: 0.65rem !important; }
    .footer-tagline { font-size: 0.75rem !important; }
    .footer-link { font-size: 0.65rem !important; letter-spacing: 1px !important; }
    .footer-info { font-size: 0.75rem !important; }
    .footer-copy { font-size: 0.7rem !important; }
    .footer-links-row { gap: 12px !important; }
    .footer-info-row { gap: 12px !important; }
}

@media (max-width: 400px) {
    .hero-title-main { font-size: 1.9rem !important; }
    .hero-title-red { font-size: 2.4rem !important; }
    .plan-price { font-size: 1.8rem !important; }
    .num-val { font-size: 1.6rem !important; }
    .sec-title { font-size: 1.6rem !important; }
    .why-grid { gap: 5px !important; }
    .pricing-grid { gap: 5px !important; }
    .contact-grid { gap: 5px !important; }
}
</style>
""", unsafe_allow_html=True)


def divider():
    st.markdown(
        '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>',
        unsafe_allow_html=True
    )


def section_header(title, highlight, subtitle):
    st.markdown(
        '<div style="text-align:center;margin-bottom:40px;">'
        f'<div class="sec-title" style="font-family:Bebas Neue,cursive;font-size:clamp(2rem,6vw,4.5rem);color:#fff;letter-spacing:4px;">'
        f'{title} <span style="color:#dc2626;">{highlight}</span>'
        '</div>'
        '<div style="width:70px;height:4px;background:linear-gradient(90deg,#dc2626,#991b1b);margin:10px auto 14px;border-radius:2px;"></div>'
        f'<div class="sec-sub" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.85rem;letter-spacing:3px;text-transform:uppercase;">{subtitle}</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ══════════════════════════════════════════════════════════════
# NAVBAR  ← marquee is INSIDE this same block, right below nav
# ══════════════════════════════════════════════════════════════
items = ["💪 TRAIN HARD", "🔥 BURN STRONGER", "⚡ NO EXCUSES",
         "🏆 CHAMPIONS BUILT HERE", "💥 PUSH YOUR LIMITS", "🎯 RESULTS GUARANTEED"]
mi = ""
for item in items * 2:
    mi += (
        f'<span class="marquee-item" style="font-family:Bebas Neue,cursive;font-size:1.1rem;'
        f'color:#fff;letter-spacing:3px;padding:0 20px;">{item}</span>'
        f'<span style="color:rgba(255,255,255,0.4);padding:0 4px;">•</span>'
    )

st.markdown(
    # ── Navbar ──
    '<div class="nav-wrap" style="background:rgba(0,0,0,0.97);border-bottom:2px solid #dc2626;'
    'padding:12px 20px;display:flex;align-items:center;justify-content:space-between;'
    'box-shadow:0 4px 25px rgba(220,38,38,0.3);position:sticky;top:0;z-index:9999;">'
    '<div class="nav-brand-text" style="font-family:Bebas Neue,cursive;font-size:1.5rem;color:#fff;letter-spacing:3px;white-space:nowrap;">'
    'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span>'
    '</div>'
    '<div class="nav-gap" style="display:flex;gap:20px;align-items:center;flex-shrink:0;">'
    '<a class="nav-link" href="#about"    style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;white-space:nowrap;">ABOUT</a>'
    '<a class="nav-link" href="#services" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;white-space:nowrap;">SERVICES</a>'
    '<a class="nav-link" href="#pricing"  style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;white-space:nowrap;">PRICING</a>'
    '<a class="nav-link" href="#schedule" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;white-space:nowrap;">SCHEDULE</a>'
    '<a class="nav-link" href="#contact"  style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;font-weight:700;white-space:nowrap;">JOIN NOW</a>'
    '</div>'
    '</div>'

    # ── Marquee directly below navbar ──
    '<div style="background:linear-gradient(90deg,#dc2626,#991b1b,#dc2626);padding:11px 0;overflow:hidden;white-space:nowrap;">'
    f'<div style="display:inline-block;animation:marquee 20s linear infinite;">{mi}</div>'
    '</div>'
    '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>',
    unsafe_allow_html=True
)


# ── HERO ────────────────────────────────────────────────────
st.markdown(
    '<div id="home" class="sec-pad" style="background:radial-gradient(ellipse at top,#1a0000 0%,#000 50%,#050505 100%);'
    'min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center;'
    'text-align:center;padding:50px 16px 40px;">'

    '<div class="hero-badge" style="background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;'
    'font-family:Oswald,sans-serif;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;'
    'padding:7px 18px;border-radius:2px;margin-bottom:24px;white-space:nowrap;">'
    'EST. 2014 — KARWAR\'S #1 FITNESS DESTINATION'
    '</div>'

    '<div class="logo-circle" style="width:150px;height:150px;border-radius:50%;'
    'background:linear-gradient(135deg,#1a1a1a,#000);border:3px solid #dc2626;'
    'display:flex;align-items:center;justify-content:center;margin:0 auto 24px auto;'
    'box-shadow:0 0 50px rgba(220,38,38,0.6);animation:glow 2s ease-in-out infinite alternate;">'
    '<div style="text-align:center;padding:8px;">'
    '<div class="logo-gym-icon" style="font-size:1.8rem;">🏋️</div>'
    '<div class="logo-name"     style="font-family:Bebas Neue,cursive;color:#fff;font-size:1rem;letter-spacing:2px;line-height:1.1;">SAMEER\'S</div>'
    '<div class="logo-ult"      style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.2rem;letter-spacing:2px;line-height:1.1;">ULTIMATE</div>'
    '<div class="logo-sub"      style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.45rem;letter-spacing:1px;">FITNESS &amp; GYM</div>'
    '</div>'
    '</div>'

    '<div class="hero-title-main" style="font-family:Bebas Neue,cursive;font-size:clamp(3rem,10vw,8rem);'
    'color:#fff;line-height:0.9;letter-spacing:4px;text-shadow:0 0 40px rgba(220,38,38,0.4);">FORGE YOUR</div>'

    '<div class="hero-title-red" style="font-family:Bebas Neue,cursive;font-size:clamp(3.5rem,13vw,10rem);'
    'color:#dc2626;line-height:0.9;letter-spacing:4px;text-shadow:0 0 60px rgba(220,38,38,0.7);margin-bottom:14px;">GREATNESS</div>'

    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:clamp(0.65rem,2vw,1rem);'
    'letter-spacing:4px;text-transform:uppercase;margin-bottom:8px;">FITNESS &amp; GYM • KARWAR, KARNATAKA</div>'

    '<div class="hero-tagline" style="font-family:Rajdhani,sans-serif;color:#f3f4f6;'
    'font-size:clamp(0.9rem,3vw,1.4rem);font-style:italic;margin-bottom:28px;">'
    '<span class="hero-tagline-quote" style="color:#dc2626;font-size:1.8rem;">"</span>'
    'A place where champions are built'
    '<span class="hero-tagline-quote" style="color:#dc2626;font-size:1.8rem;">"</span>'
    '</div>'

    '<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:40px;">'
    '<a class="hero-btn-primary" href="tel:9483834949" '
    'style="background:linear-gradient(135deg,#dc2626,#991b1b);color:#fff;font-family:Oswald,sans-serif;'
    'font-size:0.95rem;letter-spacing:2px;text-transform:uppercase;padding:14px 28px;border-radius:4px;'
    'text-decoration:none;border:2px solid #dc2626;white-space:nowrap;">📞 JOIN — 9483834949</a>'
    '<a class="hero-btn-secondary" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" '
    'style="background:transparent;color:#fff;font-family:Oswald,sans-serif;font-size:0.95rem;'
    'letter-spacing:2px;text-transform:uppercase;padding:14px 28px;border-radius:4px;'
    'text-decoration:none;border:2px solid #fff;white-space:nowrap;">📸 FOLLOW US</a>'
    '</div>'

    '<div style="display:flex;justify-content:center;flex-wrap:nowrap;">'
    '<div class="stat-divider" style="text-align:center;padding:10px 20px;border-right:1px solid #374151;">'
    '<div class="stat-number" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">10+</div>'
    '<div class="stat-label"  style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
    '</div>'
    '<div class="stat-divider" style="text-align:center;padding:10px 20px;border-right:1px solid #374151;">'
    '<div class="stat-number" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">500+</div>'
    '<div class="stat-label"  style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div class="stat-divider" style="text-align:center;padding:10px 20px;border-right:1px solid #374151;">'
    '<div class="stat-number" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">994</div>'
    '<div class="stat-label"  style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '<div class="stat-divider" style="text-align:center;padding:10px 20px;">'
    '<div class="stat-number" style="font-family:Bebas Neue,cursive;font-size:2.5rem;color:#dc2626;line-height:1;">100%</div>'
    '<div class="stat-label"  style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;">Dedication</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ── ABOUT ───────────────────────────────────────────────────
st.markdown('<div id="about" class="sec-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("ABOUT", "US", "BUILDING CHAMPIONS SINCE 2014")
st.markdown(
    '<div class="about-grid" style="display:flex;gap:40px;align-items:center;flex-wrap:wrap;max-width:1000px;margin:0 auto;">'

    '<div class="about-text" style="flex:1;min-width:0;">'
    '<p class="about-text-p" style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.05rem;line-height:1.9;margin-bottom:18px;">'
    'Welcome to <strong style="color:#dc2626;">Sameer\'s Ultimate Fitness &amp; Gym</strong> — Karwar\'s premier '
    'fitness destination, established in 2014. For over a decade, we\'ve been transforming lives, '
    'building champions, and creating a community of unstoppable athletes.'
    '</p>'
    '<p class="about-text-p" style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.05rem;line-height:1.9;margin-bottom:24px;">'
    'Located on <strong style="color:#fff;">Kodibaga Main Road, Karwar</strong>, we offer state-of-the-art '
    'equipment, expert trainers, and an electrifying atmosphere that pushes you beyond limits every day.'
    '</p>'
    '<div class="about-stats-row" style="display:flex;gap:10px;flex-wrap:wrap;">'
    '<div class="about-stat-box" style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div class="about-stat-val"   style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">10+</div>'
    '<div class="about-stat-label" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">YEARS</div>'
    '</div>'
    '<div class="about-stat-box" style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div class="about-stat-val"   style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">500+</div>'
    '<div class="about-stat-label" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">MEMBERS</div>'
    '</div>'
    '<div class="about-stat-box" style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:10px 18px;text-align:center;">'
    '<div class="about-stat-val"   style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.6rem;line-height:1;">100%</div>'
    '<div class="about-stat-label" style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.65rem;letter-spacing:2px;">RESULTS</div>'
    '</div>'
    '</div>'
    '</div>'

    '<div class="about-visual" style="flex:0 0 240px;min-width:0;">'
    '<div style="background:linear-gradient(135deg,#1a0000,#2d0000);border:2px solid #dc2626;border-radius:12px;'
    'padding:40px 20px;text-align:center;box-shadow:0 20px 60px rgba(220,38,38,0.25);">'
    '<div style="font-size:3rem;margin-bottom:10px;">🏋️</div>'
    '<div class="about-visual-name" style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.5rem;letter-spacing:4px;">SAMEER\'S</div>'
    '<div class="about-visual-ult"  style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:2.2rem;letter-spacing:4px;line-height:1;">ULTIMATE</div>'
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


# ── WHY CHOOSE US ───────────────────────────────────────────
st.markdown('<div class="sec-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("WHY", "CHOOSE US", "WHAT MAKES US KARWAR'S BEST GYM")
why_items = [
    ("🏆", "PROVEN RESULTS",     "Hundreds of success stories from real members who transformed their bodies."),
    ("💡", "EXPERT COACHING",    "Certified trainers with years of experience guiding you every step."),
    ("⚙️", "MODERN EQUIPMENT",  "State-of-the-art machines and free weights for the ultimate workout."),
    ("🔥", "INTENSE ATMOSPHERE", "An electrifying environment that keeps you motivated every day."),
    ("👥", "STRONG COMMUNITY",   "A brotherhood of fitness enthusiasts pushing each other to excel."),
    ("📍", "PRIME LOCATION",     "Conveniently located on Kodibaga Main Road, Karwar."),
]
wg = '<div class="why-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:1100px;margin:0 auto;">'
for icon, title, desc in why_items:
    wg += (
        '<div class="why-card" style="background:rgba(220,38,38,0.05);border:1px solid rgba(220,38,38,0.2);'
        'border-radius:10px;padding:24px 16px;text-align:center;">'
        f'<div class="why-icon"  style="font-size:2rem;margin-bottom:10px;">{icon}</div>'
        f'<div class="why-title" style="font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;margin-bottom:7px;">{title}</div>'
        f'<div class="why-desc"  style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.85rem;line-height:1.5;">{desc}</div>'
        '</div>'
    )
wg += '</div>'
st.markdown(wg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── SERVICES ────────────────────────────────────────────────
st.markdown('<div id="services" class="sec-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("OUR", "SERVICES", "EVERYTHING YOU NEED TO REACH YOUR PEAK")
services = [
    ("🏋️", "WEIGHT TRAINING",     "Comprehensive strength training with free weights, barbells, and machines."),
    ("🔥", "CARDIO ZONE",          "Treadmills, bikes, and ellipticals to torch calories and boost endurance."),
    ("🥊", "COMBAT FITNESS",       "Boxing bags and combat training to build endurance, agility, and power."),
    ("👤", "PERSONAL TRAINING",    "One-on-one sessions with certified trainers tailored to your goals."),
    ("🍎", "NUTRITION GUIDANCE",   "Personalized diet plans and nutritional advice for your transformation."),
    ("⚡", "HIIT CLASSES",         "High-Intensity Interval Training that maximizes fat burn in minimum time."),
    ("💪", "BODY BUILDING",        "Dedicated programs for those looking to sculpt the perfect physique."),
    ("🧘", "FLEXIBILITY & CORE",   "Stretching routines and core strengthening for performance and recovery."),
    ("📊", "BODY ASSESSMENT",      "Regular body composition analysis and progress tracking to stay on target."),
]
sg = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;max-width:1150px;margin:0 auto;">'
for icon, title, desc in services:
    sg += (
        '<div class="svc-card" style="background:linear-gradient(135deg,#111,#1a1a1a);border:1px solid #1f2937;'
        'border-top:3px solid #dc2626;border-radius:10px;padding:26px 20px;text-align:center;">'
        f'<div class="svc-icon"  style="font-size:2.2rem;margin-bottom:12px;">{icon}</div>'
        f'<div class="svc-title" style="font-family:Oswald,sans-serif;color:#fff;font-size:1rem;letter-spacing:2px;margin-bottom:9px;">{title}</div>'
        f'<div class="svc-desc"  style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;line-height:1.55;">{desc}</div>'
        '</div>'
    )
sg += '</div>'
st.markdown(sg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── STATS BANNER ────────────────────────────────────────────
st.markdown(
    '<div class="sec-pad" style="background:linear-gradient(135deg,#7f1d1d,#991b1b,#7f1d1d);padding:55px 20px;">'
    '<div style="text-align:center;margin-bottom:28px;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(1.8rem,5vw,3.5rem);color:#fff;letter-spacing:4px;">OUR NUMBERS</div>'
    '</div>'
    '<div style="display:grid;grid-template-columns:repeat(4,1fr);max-width:900px;margin:0 auto;'
    'background:#0a0a0a;border-radius:12px;overflow:hidden;border:1px solid #1f2937;">'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val"   style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">10+</div>'
    '<div class="num-label" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Years</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val"   style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">500+</div>'
    '<div class="num-label" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;border-right:1px solid #1f2937;">'
    '<div class="num-val"   style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">50+</div>'
    '<div class="num-label" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Equipment</div>'
    '</div>'
    '<div class="num-cell" style="padding:28px 10px;text-align:center;">'
    '<div class="num-val"   style="font-family:Bebas Neue,cursive;font-size:2.8rem;color:#dc2626;line-height:1;">994</div>'
    '<div class="num-label" style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
divider()


# ── PRICING ─────────────────────────────────────────────────
st.markdown('<div id="pricing" class="sec-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("MEMBERSHIP", "PLANS", "INVEST IN YOUR BEST SELF")


def pricing_card(name, price, features, featured=False):
    bg     = "linear-gradient(135deg,#1a0000,#2d0000)" if featured else "#111"
    border = "2px solid #dc2626" if featured else "1px solid #1f2937"
    shadow = "box-shadow:0 20px 60px rgba(220,38,38,0.3);" if featured else ""
    badge  = (
        '<div class="plan-badge" style="position:absolute;top:0;left:50%;transform:translateX(-50%);'
        'background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;'
        'font-family:Oswald,sans-serif;font-size:0.65rem;letter-spacing:2px;'
        'padding:5px 14px;border-radius:0 0 8px 8px;white-space:nowrap;">MOST POPULAR</div>'
    ) if featured else ""
    feats = "".join([
        f'<div class="plan-feat" style="font-family:Rajdhani,sans-serif;color:#d1d5db;padding:7px 0;'
        f'border-bottom:1px solid {"#3f0000" if featured else "#1f2937"};font-size:0.88rem;">✅ {f}</div>'
        for f in features
    ])
    return (
        f'<div class="plan-card" style="background:{bg};border:{border};border-radius:12px;'
        f'padding:28px 18px;text-align:center;{shadow}position:relative;">'
        f'{badge}'
        f'<div class="plan-name" style="font-family:Bebas Neue,cursive;font-size:1.4rem;color:#fff;'
        f'letter-spacing:2px;margin-bottom:4px;{"margin-top:16px;" if featured else ""}">{name}</div>'
        f'<div class="plan-price" style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;margin:14px 0 4px;">'
        f'<span class="plan-price-sym" style="font-family:Oswald,sans-serif;font-size:1.1rem;color:#9ca3af;vertical-align:super;">Rs.</span>{price}</div>'
        f'<div class="plan-period" style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:2px;margin-bottom:18px;">PER MONTH</div>'
        f'<div style="text-align:left;margin-bottom:20px;">{feats}</div>'
        f'<a href="tel:9483834949" class="plan-btn" style="display:block;background:linear-gradient(135deg,#dc2626,#991b1b);'
        f'color:#fff;font-family:Oswald,sans-serif;font-size:0.8rem;letter-spacing:2px;'
        f'text-transform:uppercase;padding:12px;border-radius:6px;text-decoration:none;">📞 ENROLL NOW</a>'
        f'</div>'
    )


pg  = '<div class="pricing-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:1050px;margin:0 auto;align-items:start;">'
pg += pricing_card("🥉 STARTER", "599",
                   ["Gym Access — All Equipment", "Locker Room Access", "Basic Fitness Assessment",
                    "Group Workout Sessions", "Cardio Zone Access"])
pg += pricing_card("🥇 ULTIMATE", "999",
                   ["Everything in Starter", "Personal Training (4 Sessions)", "Nutrition Consultation",
                    "Body Composition Analysis", "Progress Tracking", "Custom Diet Plan"], featured=True)
pg += pricing_card("🏆 CHAMPION", "1499",
                   ["Everything in Ultimate", "Unlimited Personal Training", "Custom Workout Programs",
                    "Advanced Nutrition Plan", "Monthly Body Analysis", "Competition Prep", "24/7 WhatsApp Support"])
pg += '</div>'
pg += ('<div style="text-align:center;margin-top:28px;">'
       '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
       'border-radius:8px;padding:11px 20px;max-width:95%;">'
       '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:2px;">'
       'QUARTERLY &amp; ANNUAL DISCOUNTS AVAILABLE — CALL 9483834949'
       '</span></div></div>')
st.markdown(pg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── SCHEDULE ────────────────────────────────────────────────
st.markdown('<div id="schedule" class="sec-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
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

sch = (
    '<div style="max-width:850px;margin:0 auto;border-radius:12px;overflow:hidden;'
    'border:1px solid #1f2937;width:100%;overflow-x:auto;">'
    '<table style="width:100%;border-collapse:collapse;min-width:320px;">'
    '<thead>'
    '<tr style="background:linear-gradient(135deg,#dc2626,#991b1b);">'
    '<th class="sched-head-cell" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">DAY</th>'
    '<th class="sched-head-cell" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">MORNING</th>'
    '<th class="sched-head-cell" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">EVENING</th>'
    '<th class="sched-head-cell" style="padding:13px 14px;font-family:Oswald,sans-serif;color:#fff;font-size:0.82rem;letter-spacing:2px;text-align:left;font-weight:600;">STATUS</th>'
    '</tr>'
    '</thead>'
    '<tbody>'
)
for day, morning, evening, status, sc_col, bg in days:
    dc = "#dc2626" if "OPEN" in status else "#6b7280"
    sch += (
        f'<tr style="background:{bg};border-bottom:1px solid #1f2937;">'
        f'<td class="sched-day"    style="padding:12px 14px;font-family:Oswald,sans-serif;color:{dc};font-size:0.82rem;letter-spacing:1px;">{day}</td>'
        f'<td class="sched-time"   style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.85rem;">{morning}</td>'
        f'<td class="sched-time"   style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.85rem;">{evening}</td>'
        f'<td class="sched-status" style="padding:12px 14px;font-family:Rajdhani,sans-serif;color:{sc_col};font-size:0.82rem;">{status}</td>'
        f'</tr>'
    )
sch += (
    '</tbody></table></div>'
    '<div style="text-align:center;margin-top:20px;">'
    '<div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);'
    'border-radius:8px;padding:11px 18px;max-width:95%;">'
    '<span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.78rem;letter-spacing:2px;">'
    'HOLIDAY HOURS MAY VARY — CALL 9483834949'
    '</span></div></div>'
)
st.markdown(sch, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── TESTIMONIALS ────────────────────────────────────────────
st.markdown('<div class="sec-pad" style="background:#000;padding:70px 20px;">', unsafe_allow_html=True)
section_header("MEMBER", "STORIES", "REAL PEOPLE. REAL RESULTS.")
testimonials = [
    ("Sameer's Gym changed my life. In just 6 months, I lost 15kg and gained incredible strength!", "RAHUL K.", "2021"),
    ("Best gym in Karwar! Electric atmosphere. Walk in tired, walk out unstoppable. Sameer sir checks your form!", "PRIYA S.", "2022"),
    ("Nutrition guidance alone was worth the fee. From 65kg to lean 72kg in 8 months. Pure muscle gains!", "VISHAL D.", "2019"),
    ("As a woman I was nervous. Environment is so welcoming and professional. Trainers are amazing!", "SNEHA R.", "2023"),
    ("Nothing compares to Sameer's. Personal training exceptional. Transformation in 3 months unbelievable!", "AKASH M.", "2020"),
    ("5:30 AM sessions are my favorite! Clean gym, pumping music, amazing community spirit. Best decision!", "ADITYA N.", "2022"),
]
tg = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px;max-width:1100px;margin:0 auto;">'
for text, author, year in testimonials:
    tg += (
        '<div class="test-card" style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:24px;border-top:3px solid #dc2626;">'
        f'<div class="test-stars"  style="color:#fbbf24;font-size:1rem;margin-bottom:8px;">★★★★★</div>'
        f'<div class="test-text"   style="font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:0.95rem;line-height:1.65;margin-bottom:14px;font-style:italic;">"{text}"</div>'
        f'<div class="test-author" style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.82rem;letter-spacing:2px;">— {author}, since {year}</div>'
        '</div>'
    )
tg += '</div>'
st.markdown(tg, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── CONTACT ─────────────────────────────────────────────────
st.markdown('<div id="contact" class="sec-pad" style="background:#050505;padding:70px 20px;">', unsafe_allow_html=True)
section_header("FIND &amp;", "CONNECT", "WE'D LOVE TO HEAR FROM YOU")

contact_cards = [
    ("📞", "CALL / WHATSAPP", "9483834949",                                                                                  "tel:9483834949"),
    ("📸", "INSTAGRAM",       "@sameers_ultimatefitness<br><span style='font-size:0.75rem;color:#6b7280;'>994 Followers</span>", "https://www.instagram.com/sameers_ultimatefitness/"),
    ("📍", "LOCATION",        "Kodibaga Main Road,<br>Karwar, Karnataka 581301",                                               "https://maps.google.com/?q=Kodibaga+Main+Road+Karwar+Karnataka+581301"),
    ("⏰", "HOURS",           "Mon–Sat: 5:30AM–9:30PM<br>Sunday: 6AM–10AM",                                                   None),
]
cg = '<div class="contact-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:1000px;margin:0 auto 45px;">'
for icon, label, val, link in contact_cards:
    inner = (
        f'<div class="contact-card" style="background:#111;border:1px solid #1f2937;border-radius:10px;'
        f'padding:24px 12px;text-align:center;border-top:3px solid #dc2626;">'
        f'<div class="contact-icon"  style="font-size:1.8rem;margin-bottom:9px;">{icon}</div>'
        f'<div class="contact-label" style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.65rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">{label}</div>'
        f'<div class="contact-val"   style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.85rem;line-height:1.5;">{val}</div>'
        f'</div>'
    )
    cg += f'<a href="{link}" target="_blank" style="text-decoration:none;">{inner}</a>' if link else inner
cg += '</div>'
st.markdown(cg, unsafe_allow_html=True)

st.markdown(
    '<div style="max-width:900px;margin:0 auto;border-radius:12px;overflow:hidden;'
    'border:2px solid #dc2626;box-shadow:0 10px 40px rgba(220,38,38,0.2);">'
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3863.87!2d74.1279!3d14.8002!'
    '2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bbe8f6d0dffffff%3A0x1!'
    '2sKodibaga%20Main%20Rd%2C%20Karwar%2C%20Karnataka%20581301!5e0!3m2!1sen!2sin!4v1700000000000" '
    'width="100%" height="280" style="border:0;display:block;" allowfullscreen="" loading="lazy"></iframe>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()


# ── CONTACT FORM ────────────────────────────────────────────
st.markdown('<div class="sec-pad" style="background:#000;padding:60px 20px 20px;">', unsafe_allow_html=True)
section_header("START YOUR", "JOURNEY", "FILL THE FORM — WE'LL CALL YOU BACK")

col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    with st.form("join_form", clear_on_submit=True):
        name  = st.text_input("YOUR FULL NAME *")
        phone = st.text_input("MOBILE NUMBER *")
        goal  = st.selectbox("YOUR FITNESS GOAL", [
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
        msg       = st.text_area("MESSAGE (OPTIONAL)", height=90, placeholder="Tell us about your fitness goals...")
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
    '<div class="sec-pad" style="background:linear-gradient(135deg,#1a0000,#dc2626,#1a0000);padding:60px 20px;text-align:center;">'
    '<div class="cta-title" style="font-family:Bebas Neue,cursive;font-size:clamp(1.8rem,7vw,5rem);'
    'color:#fff;letter-spacing:3px;text-shadow:0 4px 20px rgba(0,0,0,0.5);margin-bottom:10px;line-height:1.1;">'
    'YOUR TRANSFORMATION STARTS TODAY'
    '</div>'
    '<div class="cta-sub" style="font-family:Rajdhani,sans-serif;color:rgba(255,255,255,0.8);'
    'font-size:clamp(0.9rem,3vw,1.2rem);margin-bottom:28px;">Don\'t wait. Don\'t make excuses. <strong>START NOW.</strong></div>'
    '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">'
    '<a class="cta-btn-w" href="tel:9483834949" '
    'style="display:inline-block;background:#fff;color:#dc2626;font-family:Oswald,sans-serif;'
    'font-size:1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;'
    'padding:15px 32px;border-radius:4px;text-decoration:none;white-space:nowrap;">📞 CALL: 9483834949</a>'
    '<a class="cta-btn-t" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" '
    'style="display:inline-block;background:transparent;color:#fff;font-family:Oswald,sans-serif;'
    'font-size:1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;'
    'padding:15px 32px;border-radius:4px;text-decoration:none;border:2px solid rgba(255,255,255,0.8);white-space:nowrap;">📸 FOLLOW US</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ── FOOTER ──────────────────────────────────────────────────
st.markdown(
    '<div class="sec-pad" style="background:#000;border-top:1px solid #111;padding:40px 20px 25px;text-align:center;">'
    '<div class="footer-brand" style="font-family:Bebas Neue,cursive;font-size:2rem;color:#fff;letter-spacing:4px;margin-bottom:3px;">'
    'SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span>'
    '</div>'
    '<div class="footer-sub"     style="font-family:Oswald,sans-serif;font-size:0.8rem;color:#6b7280;letter-spacing:4px;margin-bottom:4px;">FITNESS &amp; GYM</div>'
    '<div class="footer-tagline" style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.85rem;font-style:italic;margin-bottom:20px;">"A Place Where Champions Are Built" — Est. 2014</div>'
    '<div class="footer-links-row" style="display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:18px;">'
    '<a class="footer-link" href="#about"    style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">About</a>'
    '<a class="footer-link" href="#services" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Services</a>'
    '<a class="footer-link" href="#pricing"  style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Pricing</a>'
    '<a class="footer-link" href="#schedule" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.78rem;text-transform:uppercase;">Schedule</a>'
    '<a class="footer-link" href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.78rem;">Instagram</a>'
    '<a class="footer-link" href="tel:9483834949" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.78rem;">Call Us</a>'
    '</div>'
    '<div class="footer-info-row" style="display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-bottom:20px;">'
    '<span class="footer-info" style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;">📞 9483834949</span>'
    '<span class="footer-info" style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.88rem;">📍 Kodibaga Main Road, Karwar, KA 581301</span>'
    '</div>'
    '<div style="border-top:1px solid #111;padding-top:16px;">'
    '<span class="footer-copy" style="font-family:Rajdhani,sans-serif;color:#374151;font-size:0.78rem;">'
    '© 2024 Sameer\'s Ultimate Fitness &amp; Gym. All Rights Reserved. Built with 💪 in Karwar'
    '</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)