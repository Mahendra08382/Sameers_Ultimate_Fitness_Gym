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
    padding: 30px !important;
}
@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
@keyframes glow { 0% { box-shadow: 0 0 30px rgba(220,38,38,0.5); } 100% { box-shadow: 0 0 70px rgba(220,38,38,0.9); } }
@keyframes bounce { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div style="background:rgba(0,0,0,0.97);border-bottom:2px solid #dc2626;padding:14px 40px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 4px 25px rgba(220,38,38,0.3);">'
    '<div style="font-family:Bebas Neue,cursive;font-size:1.8rem;color:#fff;letter-spacing:3px;">SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span></div>'
    '<div style="display:flex;gap:28px;">'
    '<a href="#about" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.9rem;text-transform:uppercase;">ABOUT</a>'
    '<a href="#services" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.9rem;text-transform:uppercase;">SERVICES</a>'
    '<a href="#pricing" style="font-family:Oswald,sans-serif;color:#9ca3af;text-decoration:none;letter-spacing:2px;font-size:0.9rem;text-transform:uppercase;">PRICING</a>'
    '<a href="#contact" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.9rem;text-transform:uppercase;font-weight:700;">JOIN NOW</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div id="home" style="background:radial-gradient(ellipse at top,#1a0000 0%,#000 50%,#050505 100%);min-height:92vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:60px 20px 40px;">'
    '<div style="background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;font-family:Oswald,sans-serif;font-size:0.82rem;letter-spacing:4px;text-transform:uppercase;padding:8px 24px;border-radius:2px;margin-bottom:30px;">EST. 2014 — KARWAR\'S #1 FITNESS DESTINATION</div>'
    '<div style="width:170px;height:170px;border-radius:50%;background:linear-gradient(135deg,#1a1a1a,#000);border:4px solid #dc2626;display:flex;align-items:center;justify-content:center;margin:0 auto 30px auto;box-shadow:0 0 50px rgba(220,38,38,0.6);animation:glow 2s ease-in-out infinite alternate;">'
    '<div style="text-align:center;padding:10px;">'
    '<div style="font-size:2.2rem;">🏋️</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.3rem;letter-spacing:3px;line-height:1.1;">SAMEER\'S</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.5rem;letter-spacing:2px;line-height:1.1;">ULTIMATE</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.55rem;letter-spacing:2px;">FITNESS &amp; GYM</div>'
    '</div>'
    '</div>'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(3.5rem,10vw,8rem);color:#fff;line-height:0.9;letter-spacing:4px;text-shadow:0 0 40px rgba(220,38,38,0.4);">FORGE YOUR</div>'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(4.5rem,13vw,10rem);color:#dc2626;line-height:0.9;letter-spacing:4px;text-shadow:0 0 60px rgba(220,38,38,0.7);margin-bottom:15px;">GREATNESS</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:1rem;letter-spacing:6px;text-transform:uppercase;margin-bottom:10px;">FITNESS &amp; GYM • KARWAR, KARNATAKA</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#f3f4f6;font-size:1.4rem;font-style:italic;margin-bottom:35px;"><span style="color:#dc2626;font-size:2rem;">"</span>A place where champions are built<span style="color:#dc2626;font-size:2rem;">"</span></div>'
    '<div style="display:flex;gap:18px;justify-content:center;flex-wrap:wrap;margin-bottom:50px;">'
    '<a href="tel:9483834949" style="background:linear-gradient(135deg,#dc2626,#991b1b);color:#fff;font-family:Oswald,sans-serif;font-size:1rem;letter-spacing:3px;text-transform:uppercase;padding:16px 38px;border-radius:4px;text-decoration:none;border:2px solid #dc2626;box-shadow:0 4px 20px rgba(220,38,38,0.4);">📞 JOIN NOW — 9483834949</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="background:transparent;color:#fff;font-family:Oswald,sans-serif;font-size:1rem;letter-spacing:3px;text-transform:uppercase;padding:16px 38px;border-radius:4px;text-decoration:none;border:2px solid #fff;">📸 FOLLOW US</a>'
    '</div>'
    '<div style="display:flex;justify-content:center;flex-wrap:wrap;">'
    '<div style="text-align:center;padding:10px 35px;border-right:1px solid #374151;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;">Years Strong</div>'
    '</div>'
    '<div style="text-align:center;padding:10px 35px;border-right:1px solid #374151;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;">Members</div>'
    '</div>'
    '<div style="text-align:center;padding:10px 35px;border-right:1px solid #374151;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">994</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;">Followers</div>'
    '</div>'
    '<div style="text-align:center;padding:10px 35px;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3rem;color:#dc2626;line-height:1;">100%</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.75rem;letter-spacing:3px;text-transform:uppercase;">Dedication</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="background:linear-gradient(90deg,#dc2626,#991b1b,#dc2626);padding:14px 0;overflow:hidden;white-space:nowrap;">'
    '<div style="display:inline-block;animation:marquee 22s linear infinite;">'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">💪 TRAIN HARD</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">🔥 BURN STRONGER</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">⚡ NO EXCUSES</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">🏆 CHAMPIONS BUILT HERE</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">💥 PUSH YOUR LIMITS</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">🎯 RESULTS GUARANTEED</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">💪 TRAIN HARD</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">🔥 BURN STRONGER</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">⚡ NO EXCUSES</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '<span style="font-family:Bebas Neue,cursive;font-size:1.2rem;color:#fff;letter-spacing:4px;padding:0 25px;">🏆 CHAMPIONS BUILT HERE</span>'
    '<span style="color:rgba(255,255,255,0.4);padding:0 5px;">•</span>'
    '</div>'
    '</div>'
    '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>',
    unsafe_allow_html=True
)

def section_header(title, highlight, subtitle):
    st.markdown(
        f'<div style="text-align:center;margin-bottom:50px;">'
        f'<div style="font-family:Bebas Neue,cursive;font-size:clamp(2.5rem,6vw,4.5rem);color:#fff;letter-spacing:4px;">'
        f'{title} <span style="color:#dc2626;">{highlight}</span>'
        f'</div>'
        f'<div style="width:70px;height:4px;background:linear-gradient(90deg,#dc2626,#991b1b);margin:12px auto 15px;border-radius:2px;"></div>'
        f'<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.9rem;letter-spacing:4px;text-transform:uppercase;">{subtitle}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def divider():
    st.markdown('<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);"></div>', unsafe_allow_html=True)

def card(icon, title, desc, bg="#111", border_color="#dc2626"):
    return (
        f'<div style="background:{bg};border:1px solid #1f2937;border-top:3px solid {border_color};'
        f'border-radius:10px;padding:35px 28px;text-align:center;">'
        f'<div style="font-size:3rem;margin-bottom:18px;">{icon}</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#fff;font-size:1.2rem;letter-spacing:2px;margin-bottom:12px;text-transform:uppercase;">{title}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:1rem;line-height:1.6;">{desc}</div>'
        f'</div>'
    )

st.markdown('<div id="about" style="background:#050505;padding:80px 40px;">', unsafe_allow_html=True)
section_header("ABOUT", "US", "BUILDING CHAMPIONS SINCE 2014")
st.markdown(
    '<div style="max-width:1000px;margin:0 auto;display:flex;gap:50px;align-items:center;flex-wrap:wrap;">'
    '<div style="flex:1;min-width:280px;">'
    '<p style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.1rem;line-height:1.9;margin-bottom:20px;">'
    'Welcome to <strong style="color:#dc2626;">Sameer\'s Ultimate Fitness &amp; Gym</strong> — Karwar\'s premier '
    'fitness destination, established in 2014. For over a decade, we\'ve been transforming lives, '
    'building champions, and creating a community of unstoppable athletes.'
    '</p>'
    '<p style="font-family:Rajdhani,sans-serif;color:#9ca3af;font-size:1.1rem;line-height:1.9;margin-bottom:30px;">'
    'Located on <strong style="color:#fff;">Kodibaga Main Road, Karwar</strong>, we offer state-of-the-art '
    'equipment, expert trainers, and an electrifying atmosphere that pushes you beyond limits every day.'
    '</p>'
    '<div style="display:flex;gap:12px;flex-wrap:wrap;">'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:12px 22px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.8rem;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.7rem;letter-spacing:2px;">YEARS</div>'
    '</div>'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:12px 22px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.8rem;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.7rem;letter-spacing:2px;">MEMBERS</div>'
    '</div>'
    '<div style="background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.35);border-radius:6px;padding:12px 22px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:1.8rem;line-height:1;">100%</div>'
    '<div style="font-family:Oswald,sans-serif;color:#9ca3af;font-size:0.7rem;letter-spacing:2px;">RESULTS</div>'
    '</div>'
    '</div>'
    '</div>'
    '<div style="flex:0 0 280px;min-width:250px;">'
    '<div style="background:linear-gradient(135deg,#1a0000,#2d0000);border:2px solid #dc2626;border-radius:12px;padding:50px 30px;text-align:center;box-shadow:0 20px 60px rgba(220,38,38,0.25);">'
    '<div style="font-size:4rem;margin-bottom:15px;">🏋️</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.8rem;letter-spacing:4px;">SAMEER\'S</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#dc2626;font-size:2.8rem;letter-spacing:4px;line-height:1;">ULTIMATE</div>'
    '<div style="height:2px;background:linear-gradient(90deg,transparent,#dc2626,transparent);margin:15px 0;"></div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:4px;">FITNESS &amp; GYM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.75rem;letter-spacing:2px;margin-top:5px;">EST 2014</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div style="background:#000;padding:80px 40px;">', unsafe_allow_html=True)
section_header("WHY", "CHOOSE US", "WHAT MAKES US KARWAR'S BEST GYM")
why_cards = [
    ("🏆", "PROVEN RESULTS", "Hundreds of success stories from real members who transformed their bodies and lives."),
    ("💡", "EXPERT COACHING", "Certified trainers with years of experience guiding you every step of the way."),
    ("⚙️", "MODERN EQUIPMENT", "State-of-the-art machines and free weights for the ultimate workout experience."),
    ("🔥", "INTENSE ATMOSPHERE", "An electrifying environment that keeps you motivated and hungry for more."),
    ("👥", "STRONG COMMUNITY", "A brotherhood of fitness enthusiasts who push each other to excel every day."),
    ("📍", "PRIME LOCATION", "Conveniently located on Kodibaga Main Road, easy to reach from anywhere in Karwar."),
]
grid = '<div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;">'
for icon, title, desc in why_cards:
    grid += (
        f'<div style="background:rgba(220,38,38,0.05);border:1px solid rgba(220,38,38,0.2);'
        f'border-radius:10px;padding:30px 22px;text-align:center;">'
        f'<div style="font-size:2.5rem;margin-bottom:14px;">{icon}</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#fff;font-size:1.1rem;letter-spacing:2px;margin-bottom:10px;">{title}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.95rem;line-height:1.6;">{desc}</div>'
        f'</div>'
    )
grid += '</div>'
st.markdown(grid, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div id="services" style="background:#050505;padding:80px 40px;">', unsafe_allow_html=True)
section_header("OUR", "SERVICES", "EVERYTHING YOU NEED TO REACH YOUR PEAK")
services = [
    ("🏋️", "WEIGHT TRAINING", "Comprehensive strength training with free weights, barbells, and machines for all levels."),
    ("🔥", "CARDIO ZONE", "High-intensity cardio equipment — treadmills, bikes, and ellipticals to torch calories."),
    ("🥊", "COMBAT FITNESS", "Boxing bags and combat training to build endurance, agility, and explosive power."),
    ("👤", "PERSONAL TRAINING", "One-on-one sessions with certified trainers tailored specifically to your fitness goals."),
    ("🍎", "NUTRITION GUIDANCE", "Personalized diet plans and nutritional advice to fuel your transformation effectively."),
    ("⚡", "HIIT CLASSES", "High-Intensity Interval Training that maximizes fat burn in minimum time."),
    ("💪", "BODY BUILDING", "Dedicated bodybuilding programs for those looking to sculpt the perfect physique."),
    ("🧘", "FLEXIBILITY & CORE", "Stretching routines and core strengthening to enhance performance and recovery."),
    ("📊", "BODY ASSESSMENT", "Regular body composition analysis and progress tracking to keep you on target."),
]
sgrid = '<div style="max-width:1150px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:22px;">'
for icon, title, desc in services:
    sgrid += card(icon, title, desc)
sgrid += '</div>'
st.markdown(sgrid, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown(
    '<div style="background:linear-gradient(135deg,#7f1d1d,#991b1b,#7f1d1d);padding:60px 40px;">'
    '<div style="text-align:center;margin-bottom:40px;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(2rem,5vw,3.5rem);color:#fff;letter-spacing:4px;">OUR NUMBERS</div>'
    '</div>'
    '<div style="max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));background:#0a0a0a;border-radius:12px;overflow:hidden;border:1px solid #1f2937;">'
    '<div style="padding:40px 20px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3.5rem;color:#dc2626;line-height:1;">10+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;">Years of Excellence</div>'
    '</div>'
    '<div style="padding:40px 20px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3.5rem;color:#dc2626;line-height:1;">500+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;">Happy Members</div>'
    '</div>'
    '<div style="padding:40px 20px;text-align:center;border-right:1px solid #1f2937;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3.5rem;color:#dc2626;line-height:1;">50+</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;">Equipment Pieces</div>'
    '</div>'
    '<div style="padding:40px 20px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:3.5rem;color:#dc2626;line-height:1;">994</div>'
    '<div style="font-family:Oswald,sans-serif;color:#6b7280;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;">Instagram Followers</div>'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
divider()

st.markdown('<div id="pricing" style="background:#000;padding:80px 40px;">', unsafe_allow_html=True)
section_header("MEMBERSHIP", "PLANS", "INVEST IN YOUR BEST SELF")

def pricing_card(name, price, period, features, featured=False):
    bg = "linear-gradient(135deg,#1a0000,#2d0000)" if featured else "#111"
    border = "2px solid #dc2626" if featured else "1px solid #1f2937"
    shadow = "box-shadow:0 20px 60px rgba(220,38,38,0.3);" if featured else ""
    mt = "margin-top:-15px;" if featured else ""
    badge = '<div style="position:absolute;top:0;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,#dc2626,#991b1b);color:#fff;font-family:Oswald,sans-serif;font-size:0.75rem;letter-spacing:2px;padding:6px 22px;border-radius:0 0 8px 8px;">MOST POPULAR</div>' if featured else ""
    feats = "".join([f'<div style="font-family:Rajdhani,sans-serif;color:#d1d5db;padding:9px 0;border-bottom:1px solid {"#3f0000" if featured else "#1f2937"};font-size:1rem;">✅ {f}</div>' for f in features])
    return (
        f'<div style="background:{bg};border:{border};border-radius:12px;padding:40px 30px;text-align:center;{shadow}{mt}position:relative;">'
        f'{badge}'
        f'<div style="font-family:Bebas Neue,cursive;font-size:1.8rem;color:#fff;letter-spacing:3px;margin-bottom:5px;{"margin-top:20px;" if featured else ""}">{name}</div>'
        f'<div style="font-family:Bebas Neue,cursive;font-size:4rem;color:#dc2626;line-height:1;margin:20px 0 5px;"><span style="font-family:Oswald,sans-serif;font-size:1.5rem;color:#9ca3af;vertical-align:super;">Rs.</span>{price}</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.85rem;letter-spacing:2px;margin-bottom:25px;">{period}</div>'
        f'<div style="text-align:left;margin-bottom:30px;">{feats}</div>'
        f'<a href="tel:9483834949" style="display:block;background:linear-gradient(135deg,#dc2626,#991b1b);color:#fff;font-family:Oswald,sans-serif;font-size:0.95rem;letter-spacing:3px;text-transform:uppercase;padding:14px;border-radius:6px;text-decoration:none;">📞 ENROLL NOW</a>'
        f'</div>'
    )

plans_html = '<div style="max-width:1050px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;align-items:start;">'
plans_html += pricing_card("🥉 STARTER", "599", "PER MONTH", ["Gym Access — All Equipment", "Locker Room Access", "Basic Fitness Assessment", "Group Workout Sessions", "Cardio Zone Access"])
plans_html += pricing_card("🥇 ULTIMATE", "999", "PER MONTH", ["Everything in Starter", "Personal Training (4 Sessions)", "Nutrition Consultation", "Body Composition Analysis", "Progress Tracking", "Custom Diet Plan"], featured=True)
plans_html += pricing_card("🏆 CHAMPION", "1499", "PER MONTH", ["Everything in Ultimate", "Unlimited Personal Training", "Custom Workout Programs", "Advanced Nutrition Plan", "Monthly Body Analysis", "Competition Prep", "24/7 WhatsApp Support"])
plans_html += '</div>'
plans_html += '<div style="text-align:center;margin-top:35px;"><div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);border-radius:8px;padding:14px 28px;"><span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.95rem;letter-spacing:3px;">QUARTERLY &amp; ANNUAL DISCOUNTS AVAILABLE — CALL 9483834949</span></div></div>'
st.markdown(plans_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div id="schedule" style="background:#050505;padding:80px 40px;">', unsafe_allow_html=True)
section_header("GYM", "SCHEDULE", "WE'RE OPEN WHEN YOU NEED US")

days = [
    ("MONDAY",    "5:30 AM – 10:00 AM", "4:00 PM – 9:30 PM", "✅ OPEN",    "#10b981", "#111"),
    ("TUESDAY",   "5:30 AM – 10:00 AM", "4:00 PM – 9:30 PM", "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("WEDNESDAY", "5:30 AM – 10:00 AM", "4:00 PM – 9:30 PM", "✅ OPEN",    "#10b981", "#111"),
    ("THURSDAY",  "5:30 AM – 10:00 AM", "4:00 PM – 9:30 PM", "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("FRIDAY",    "5:30 AM – 10:00 AM", "4:00 PM – 9:30 PM", "✅ OPEN",    "#10b981", "#111"),
    ("SATURDAY",  "5:30 AM – 11:00 AM", "4:00 PM – 8:00 PM", "✅ OPEN",    "#10b981", "#0a0a0a"),
    ("SUNDAY",    "6:00 AM – 10:00 AM", "Closed",             "⚡ LIMITED", "#fbbf24", "#111"),
]

sched = '<div style="max-width:850px;margin:0 auto;border-radius:12px;overflow:hidden;border:1px solid #1f2937;">'
sched += (
    '<div style="display:grid;grid-template-columns:1.5fr 1.5fr 1.5fr 1fr;background:linear-gradient(135deg,#dc2626,#991b1b);">'
    '<div style="padding:16px 20px;font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;">DAY</div>'
    '<div style="padding:16px 20px;font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;">MORNING</div>'
    '<div style="padding:16px 20px;font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;">EVENING</div>'
    '<div style="padding:16px 20px;font-family:Oswald,sans-serif;color:#fff;font-size:0.95rem;letter-spacing:2px;">STATUS</div>'
    '</div>'
)
for day, morning, evening, status, sc, bg in days:
    dc = "#dc2626" if status == "✅ OPEN" else "#6b7280"
    sched += (
        f'<div style="display:grid;grid-template-columns:1.5fr 1.5fr 1.5fr 1fr;background:{bg};border-bottom:1px solid #1f2937;">'
        f'<div style="padding:15px 20px;font-family:Oswald,sans-serif;color:{dc};font-size:0.95rem;letter-spacing:1px;">{day}</div>'
        f'<div style="padding:15px 20px;font-family:Rajdhani,sans-serif;color:#d1d5db;">{morning}</div>'
        f'<div style="padding:15px 20px;font-family:Rajdhani,sans-serif;color:#d1d5db;">{evening}</div>'
        f'<div style="padding:15px 20px;font-family:Rajdhani,sans-serif;color:{sc};">{status}</div>'
        f'</div>'
    )
sched += '</div>'
sched += '<div style="text-align:center;margin-top:25px;"><div style="display:inline-block;background:rgba(220,38,38,0.1);border:1px solid rgba(220,38,38,0.3);border-radius:8px;padding:13px 25px;"><span style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.9rem;letter-spacing:2px;">HOLIDAY HOURS MAY VARY — CALL 9483834949</span></div></div>'
st.markdown(sched, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div style="background:#000;padding:80px 40px;">', unsafe_allow_html=True)
section_header("MEMBER", "STORIES", "REAL PEOPLE. REAL RESULTS.")
testimonials = [
    ("Sameer's Ultimate Gym completely changed my life. In just 6 months, I lost 15kg and gained incredible strength. The trainers are motivating and equipment is top-notch!", "RAHUL K.", "2021"),
    ("Best gym in Karwar, no doubt! The atmosphere is electric. You walk in feeling tired and walk out feeling unstoppable. Sameer sir personally checks your form — that's rare!", "PRIYA S.", "2022"),
    ("The nutrition guidance alone was worth the membership fee. Combined with training I went from 65kg to a lean 72kg in 8 months. Pure muscle mass gains!", "VISHAL D.", "2019"),
    ("As a woman, I was nervous about joining a gym. The environment is so welcoming and professional. The trainers are respectful and incredibly knowledgeable. Love this place!", "SNEHA R.", "2023"),
    ("I've tried many gyms but nothing compares to Sameer's. The personal training program is exceptional. My body transformation in 3 months was unbelievable!", "AKASH M.", "2020"),
    ("Early morning sessions at 5:30 AM are my favorite! The gym is clean, music is pumping, and community spirit is amazing. Best decision I ever made!", "ADITYA N.", "2022"),
]
tgrid = '<div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;">'
for text, author, year in testimonials:
    tgrid += (
        f'<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:30px;border-top:3px solid #dc2626;">'
        f'<div style="color:#fbbf24;font-size:1.1rem;margin-bottom:8px;">★★★★★</div>'
        f'<div style="font-family:Rajdhani,sans-serif;color:#d1d5db;font-size:1.05rem;line-height:1.7;margin-bottom:18px;font-style:italic;">"{text}"</div>'
        f'<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.9rem;letter-spacing:2px;">— {author}, Member since {year}</div>'
        f'</div>'
    )
tgrid += '</div>'
st.markdown(tgrid, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div id="contact" style="background:#050505;padding:80px 40px;">', unsafe_allow_html=True)
section_header("FIND &amp;", "CONNECT", "WE'D LOVE TO HEAR FROM YOU")
st.markdown(
    '<div style="max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-bottom:50px;">'
    '<a href="tel:9483834949" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:30px 20px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2.5rem;margin-bottom:12px;">📞</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;margin-bottom:8px;">CALL / WHATSAPP</div>'
    '<div style="font-family:Bebas Neue,cursive;color:#fff;font-size:1.8rem;letter-spacing:3px;">9483834949</div>'
    '</div>'
    '</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:30px 20px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2.5rem;margin-bottom:12px;">📸</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:3px;margin-bottom:8px;">INSTAGRAM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:1rem;">@sameers_ultimatefitness</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.85rem;margin-top:5px;">994 Followers</div>'
    '</div>'
    '</a>'
    '<a href="https://maps.google.com/?q=Kodibaga+Main+Road+Karwar+Karnataka+581301" target="_blank" style="text-decoration:none;">'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:30px 20px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2.5rem;margin-bottom:12px;">📍</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:3px;margin-bottom:8px;">LOCATION</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.95rem;line-height:1.5;">Kodibaga Main Road,<br>Karwar, Karnataka 581301</div>'
    '</div>'
    '</a>'
    '<div style="background:#111;border:1px solid #1f2937;border-radius:10px;padding:30px 20px;text-align:center;border-top:3px solid #dc2626;">'
    '<div style="font-size:2.5rem;margin-bottom:12px;">⏰</div>'
    '<div style="font-family:Oswald,sans-serif;color:#dc2626;font-size:0.8rem;letter-spacing:3px;margin-bottom:8px;">HOURS</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#fff;font-size:0.95rem;line-height:1.5;">Mon–Sat: 5:30AM–9:30PM<br>Sunday: 6AM–10AM</div>'
    '</div>'
    '</div>'
    '<div style="max-width:900px;margin:0 auto;border-radius:12px;overflow:hidden;border:2px solid #dc2626;box-shadow:0 10px 40px rgba(220,38,38,0.2);">'
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3863.87!2d74.1279!3d14.8002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bbe8f6d0dffffff%3A0x1!2sKodibaga%20Main%20Rd%2C%20Karwar%2C%20Karnataka%20581301!5e0!3m2!1sen!2sin!4v1700000000000" width="100%" height="380" style="border:0;display:block;" allowfullscreen="" loading="lazy"></iframe>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
divider()

st.markdown('<div style="background:#000;padding:60px 40px 20px;">', unsafe_allow_html=True)
section_header("START YOUR", "JOURNEY", "FILL THE FORM — WE'LL CALL YOU BACK")

col1, col2, col3 = st.columns([1, 2.5, 1])
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
        msg = st.text_area("MESSAGE (OPTIONAL)", height=100, placeholder="Tell us about your fitness goals...")
        submitted = st.form_submit_button("💪 SEND — LET'S GET STARTED!")
        if submitted:
            if name.strip() and phone.strip():
                st.success(f"✅ Awesome {name.upper()}! We'll call you on {phone} within 24 hours. Get ready to transform! 💪")
                st.balloons()
            else:
                st.error("⚠️ Please enter your name and phone number.")

st.markdown('<div style="padding-bottom:60px;"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="background:linear-gradient(135deg,#1a0000,#dc2626,#1a0000);padding:70px 40px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:clamp(2rem,7vw,5.5rem);color:#fff;letter-spacing:4px;text-shadow:0 4px 20px rgba(0,0,0,0.5);margin-bottom:10px;">YOUR TRANSFORMATION STARTS TODAY</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:rgba(255,255,255,0.8);font-size:1.2rem;margin-bottom:35px;letter-spacing:2px;">Don\'t wait for Monday. Don\'t wait for the new year. START NOW.</div>'
    '<div style="display:flex;gap:18px;justify-content:center;flex-wrap:wrap;">'
    '<a href="tel:9483834949" style="display:inline-block;background:#fff;color:#dc2626;font-family:Oswald,sans-serif;font-size:1.1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;padding:18px 45px;border-radius:4px;text-decoration:none;box-shadow:0 8px 30px rgba(0,0,0,0.3);">📞 CALL: 9483834949</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="display:inline-block;background:transparent;color:#fff;font-family:Oswald,sans-serif;font-size:1.1rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;padding:18px 45px;border-radius:4px;text-decoration:none;border:2px solid rgba(255,255,255,0.8);">📸 FOLLOW US</a>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="background:#000;border-top:1px solid #111;padding:50px 40px 30px;text-align:center;">'
    '<div style="font-family:Bebas Neue,cursive;font-size:2.2rem;color:#fff;letter-spacing:4px;margin-bottom:3px;">SAMEER\'S <span style="color:#dc2626;">ULTIMATE</span></div>'
    '<div style="font-family:Oswald,sans-serif;font-size:0.85rem;color:#6b7280;letter-spacing:5px;margin-bottom:5px;">FITNESS &amp; GYM</div>'
    '<div style="font-family:Rajdhani,sans-serif;color:#4b5563;font-size:0.9rem;font-style:italic;margin-bottom:25px;">"A Place Where Champions Are Built" — Est. 2014</div>'
    '<div style="display:flex;justify-content:center;gap:25px;flex-wrap:wrap;margin-bottom:25px;">'
    '<a href="#home" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">Home</a>'
    '<a href="#about" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">About</a>'
    '<a href="#services" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">Services</a>'
    '<a href="#pricing" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">Pricing</a>'
    '<a href="#schedule" style="font-family:Oswald,sans-serif;color:#4b5563;text-decoration:none;letter-spacing:2px;font-size:0.85rem;text-transform:uppercase;">Schedule</a>'
    '<a href="https://www.instagram.com/sameers_ultimatefitness/" target="_blank" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.85rem;">Instagram</a>'
    '<a href="tel:9483834949" style="font-family:Oswald,sans-serif;color:#dc2626;text-decoration:none;letter-spacing:2px;font-size:0.85rem;">Call Us</a>'
    '</div>'
    '<div style="display:flex;justify-content:center;gap:30px;flex-wrap:wrap;margin-bottom:25px;">'
    '<span style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.95rem;">📞 9483834949</span>'
    '<span style="color:#374151;">|</span>'
    '<span style="font-family:Rajdhani,sans-serif;color:#6b7280;font-size:0.95rem;">📍 Kodibaga Main Road, Karwar, Karnataka 581301</span>'
    '</div>'
    '<div style="border-top:1px solid #111;padding-top:20px;font-family:Rajdhani,sans-serif;color:#374151;font-size:0.85rem;">'
    '© 2024 Sameer\'s Ultimate Fitness &amp; Gym. All Rights Reserved. Built with 💪 in Karwar'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)