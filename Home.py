import streamlit as st
from PIL import Image
import os
import base64
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sidebar import apply_sidebar_styles, render_sidebar

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Apply sidebar styles
apply_sidebar_styles()

# Page configuration
st.set_page_config(
    page_title="Robert Macatiag | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Boyish/Tactical Dark Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Black+Ops+One&display=swap');

/* ─── Reset & Global ─────────────────────────────────── */
* { box-sizing: border-box; margin: 0; padding: 0; }

.main {
    background:
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 40px,
            rgba(0, 255, 65, 0.015) 40px,
            rgba(0, 255, 65, 0.015) 41px
        ),
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 40px,
            rgba(0, 255, 65, 0.015) 40px,
            rgba(0, 255, 65, 0.015) 41px
        ),
        linear-gradient(180deg, #050A05 0%, #070D0A 40%, #050A08 70%, #030703 100%);
    min-height: 100vh;
}

.block-container {
    padding-top: 0.5rem !important;
    max-width: 1400px !important;
}

/* ─── Scanline overlay ───────────────────────────────── */
.main::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.03) 0px,
        rgba(0, 0, 0, 0.03) 1px,
        transparent 1px,
        transparent 3px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ─── HERO CONTAINER ─────────────────────────────────── */
.hero-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 2.5rem 3rem 2rem 3rem;
    min-height: 88vh;
    gap: 4rem;
    position: relative;
    overflow: hidden;
}

/* Corner bracket decorations */
.hero-container::before {
    content: '';
    position: absolute;
    top: 20px; left: 20px;
    width: 60px; height: 60px;
    border-top: 3px solid #00FF41;
    border-left: 3px solid #00FF41;
    opacity: 0.6;
    pointer-events: none;
}

.hero-container::after {
    content: '';
    position: absolute;
    bottom: 20px; right: 20px;
    width: 60px; height: 60px;
    border-bottom: 3px solid #00FF41;
    border-right: 3px solid #00FF41;
    opacity: 0.4;
    pointer-events: none;
}

/* ─── HERO CONTENT ───────────────────────────────────── */
.hero-content {
    flex: 1;
    max-width: 660px;
    position: relative;
    z-index: 1;
}

/* Status bar */
.status-bar {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1.4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #555;
    letter-spacing: 1px;
}

.status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #00FF41;
    box-shadow: 0 0 8px #00FF41;
    animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 4px #00FF41; opacity: 1; }
    50% { box-shadow: 0 0 14px #00FF41, 0 0 28px rgba(0,255,65,0.4); opacity: 0.8; }
}

.status-text {
    color: #00FF41;
    text-transform: uppercase;
    letter-spacing: 3px;
}

.status-sep { color: #333; }

.status-id {
    color: #FF6B00;
    font-weight: 600;
}

/* Greeting prompt */
.hero-greeting {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: #00FF41;
    letter-spacing: 2px;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.prompt-symbol {
    color: #FF6B00;
    font-weight: 800;
    font-size: 1rem;
}

/* Main title */
.hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.4rem;
    font-weight: 500;
    color: #556;
    text-transform: uppercase;
    letter-spacing: 8px;
    margin-bottom: 0.4rem;
    padding-left: 4px;
}

/* Name */
.typing-name {
    font-family: 'Black Ops One', cursive;
    font-size: 4.2rem;
    font-weight: 400;
    color: #E8F5E9;
    line-height: 1.05;
    margin-bottom: 0.5rem;
    letter-spacing: 3px;
    text-shadow:
        0 0 40px rgba(0, 255, 65, 0.15),
        2px 2px 0px #1A2A1A,
        4px 4px 0px #0D180D;
    position: relative;
    display: inline-block;
}

/* Accent underline bar */
.name-underline {
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 30%, #00FF41 60%, transparent 100%);
    margin-bottom: 1.4rem;
    position: relative;
    clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
}

/* Role badge */
.role-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(255, 107, 0, 0.08);
    border: 1px solid rgba(255, 107, 0, 0.3);
    border-left: 4px solid #FF6B00;
    padding: 0.5rem 1.2rem;
    margin-bottom: 1.6rem;
    clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 50%, calc(100% - 10px) 100%, 0 100%);
}

.role-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #FF8C00;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
}

/* Description */
.hero-description {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: #4A7A4A;
    line-height: 2;
    margin-bottom: 2rem;
    max-width: 560px;
    padding: 1.2rem 1.4rem;
    background: rgba(0, 255, 65, 0.02);
    border: 1px solid #1A2E1A;
    border-left: 3px solid #2A4A2A;
    position: relative;
}

.hero-description::before {
    content: '// ABOUT';
    position: absolute;
    top: -10px; left: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #00FF41;
    background: #050A05;
    padding: 0 6px;
    letter-spacing: 2px;
}

/* Tags */
.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 2rem;
}

.tag {
    background: transparent;
    color: #00FF41;
    padding: 0.45rem 1rem;
    font-size: 0.78rem;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid #1E3D1E;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.25s ease;
    clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
    position: relative;
}

.tag::before {
    content: '#';
    color: #FF6B00;
    margin-right: 3px;
}

.tag:hover {
    background: rgba(0, 255, 65, 0.08);
    color: #00FF41;
    border-color: #00FF41;
    box-shadow: 0 0 12px rgba(0, 255, 65, 0.15);
    transform: translateY(-2px) skewX(-2deg);
}

/* CTA Button */
.cta-button {
    background: linear-gradient(135deg, #FF6B00 0%, #CC5500 50%, #AA4400 100%);
    color: #050A05;
    padding: 1rem 2.4rem;
    text-decoration: none;
    font-weight: 800;
    font-size: 0.9rem;
    font-family: 'JetBrains Mono', monospace;
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    letter-spacing: 2px;
    text-transform: uppercase;
    clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%, 16px 50%);
    box-shadow: 0 0 0 1px rgba(255, 107, 0, 0.5), 0 8px 30px rgba(255, 107, 0, 0.25);
    position: relative;
    overflow: hidden;
}

.cta-button::after {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    width: 0; height: 0;
    background: rgba(255,255,255,0.15);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition: width 0.5s ease, height 0.5s ease;
}

.cta-button:hover::after {
    width: 300px; height: 300px;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 0 1px rgba(255, 107, 0, 0.8), 0 12px 40px rgba(255, 107, 0, 0.4), 0 0 60px rgba(255, 107, 0, 0.1);
    color: #050A05;
}

.cta-button:active { transform: translateY(-1px); }

/* Social Links */
.social-links {
    display: flex;
    gap: 0.7rem;
    margin-top: 1.6rem;
    align-items: center;
}

.social-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #333;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-right: 0.3rem;
}

.social-icon {
    width: 44px; height: 44px;
    background: rgba(0,0,0,0.6);
    border: 1px solid #1E3D1E;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    cursor: pointer;
    text-decoration: none !important;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    position: relative;
}

.social-icon::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,255,65,0.05), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.social-icon:hover::before { opacity: 1; }

.social-icon:hover {
    border-color: #00FF41;
    box-shadow: 0 0 16px rgba(0, 255, 65, 0.2), inset 0 0 8px rgba(0,255,65,0.05);
    transform: translateY(-4px);
}

.social-icon:hover svg { stroke: #00FF41 !important; }
.social-icon svg { transition: stroke 0.3s ease; }

/* ─── PROFILE IMAGE SECTION ──────────────────────────── */
.hero-image {
    flex: 0 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    z-index: 1;
}

/* HUD frame */
.profile-frame {
    position: relative;
    width: 380px;
    height: 490px;
}

/* Outer tactical frame */
.profile-frame-outer {
    position: absolute;
    inset: 0;
    border: 2px solid #1A3A1A;
    clip-path: polygon(
        0 20px, 20px 0,
        calc(100% - 20px) 0, 100% 20px,
        100% calc(100% - 20px), calc(100% - 20px) 100%,
        20px 100%, 0 calc(100% - 20px)
    );
}

/* Glowing corner pieces */
.corner-tl, .corner-tr, .corner-bl, .corner-br {
    position: absolute;
    width: 30px; height: 30px;
    z-index: 3;
}

.corner-tl {
    top: -2px; left: -2px;
    border-top: 3px solid #00FF41;
    border-left: 3px solid #00FF41;
    box-shadow: -3px -3px 12px rgba(0,255,65,0.4), inset 3px 3px 8px rgba(0,255,65,0.1);
}

.corner-tr {
    top: -2px; right: -2px;
    border-top: 3px solid #FF6B00;
    border-right: 3px solid #FF6B00;
    box-shadow: 3px -3px 12px rgba(255,107,0,0.4);
}

.corner-bl {
    bottom: -2px; left: -2px;
    border-bottom: 3px solid #FF6B00;
    border-left: 3px solid #FF6B00;
    box-shadow: -3px 3px 12px rgba(255,107,0,0.4);
}

.corner-br {
    bottom: -2px; right: -2px;
    border-bottom: 3px solid #00FF41;
    border-right: 3px solid #00FF41;
    box-shadow: 3px 3px 12px rgba(0,255,65,0.4);
}

/* Image wrapper */
.profile-inner {
    position: absolute;
    inset: 6px;
    overflow: hidden;
    background: #050A05;
    clip-path: polygon(
        0 18px, 18px 0,
        calc(100% - 18px) 0, 100% 18px,
        100% calc(100% - 18px), calc(100% - 18px) 100%,
        18px 100%, 0 calc(100% - 18px)
    );
}

.profile-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 20%;
    display: block;
    filter: contrast(1.05) saturate(0.85);
}

/* HUD overlay on image */
.hud-overlay {
    position: absolute;
    inset: 6px;
    pointer-events: none;
    z-index: 2;
    clip-path: polygon(
        0 18px, 18px 0,
        calc(100% - 18px) 0, 100% 18px,
        100% calc(100% - 18px), calc(100% - 18px) 100%,
        18px 100%, 0 calc(100% - 18px)
    );
}

/* Scan line animation */
.scan-line {
    position: absolute;
    left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(0,255,65,0.5), transparent);
    animation: scan 4s linear infinite;
    top: 0;
}

@keyframes scan {
    0% { top: 0%; opacity: 1; }
    90% { opacity: 0.5; }
    100% { top: 100%; opacity: 0; }
}

/* Bottom HUD bar */
.hud-bar {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    background: linear-gradient(0deg, rgba(5,10,5,0.95) 0%, rgba(5,10,5,0.6) 60%, transparent 100%);
    padding: 1.2rem 1rem 0.8rem;
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
}

.hud-name {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00FF41;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.hud-stats {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.hud-stat {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #2A5A2A;
}

.hud-stat span {
    color: #FF6B00;
}

/* Floating side elements */
.side-panel {
    position: absolute;
    right: -50px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    z-index: 4;
}

.side-tick {
    width: 28px; height: 3px;
    background: #1E3D1E;
    transition: all 0.3s ease;
}

.side-tick.active { background: #00FF41; box-shadow: 0 0 6px #00FF41; }
.side-tick.semi { background: #FF6B00; width: 18px; }

/* Ammo/data indicators (left side) */
.left-panel {
    position: absolute;
    left: -50px;
    top: 30px;
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
}

.data-block {
    writing-mode: vertical-lr;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: #1E3D1E;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ─── FEATURE CARDS ──────────────────────────────────── */
.feature-card {
    background: rgba(5, 12, 5, 0.95);
    padding: 2rem 1.8rem;
    text-align: left;
    border: 1px solid #152515;
    border-top: 3px solid;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
    height: 100%;
    clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 14px 100%, 0 calc(100% - 14px));
}

.feature-card::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 14px; height: 14px;
    background: #00FF41;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.3;
    transition: opacity 0.3s ease;
}

.feature-card:hover::after { opacity: 0.8; }

.feature-card-1 { border-top-color: #00FF41; }
.feature-card-2 { border-top-color: #FF6B00; }
.feature-card-3 { border-top-color: #4A9EFF; }

.feature-card:hover {
    transform: translateY(-6px);
    border-color: #2A4A2A;
}

.feature-card-1:hover { box-shadow: 0 12px 40px rgba(0,255,65,0.1), 0 0 0 1px rgba(0,255,65,0.15); }
.feature-card-2:hover { box-shadow: 0 12px 40px rgba(255,107,0,0.1), 0 0 0 1px rgba(255,107,0,0.15); }
.feature-card-3:hover { box-shadow: 0 12px 40px rgba(74,158,255,0.1), 0 0 0 1px rgba(74,158,255,0.15); }

.feature-icon {
    width: 56px; height: 56px;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0,0,0,0.4);
    border: 1px solid;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    transition: transform 0.3s ease;
}

.feature-icon-1 { border-color: #00FF41; }
.feature-icon-2 { border-color: #FF6B00; }
.feature-icon-3 { border-color: #4A9EFF; }

.feature-card:hover .feature-icon { transform: scale(1.08); }

.feature-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #333;
    letter-spacing: 2px;
    margin-bottom: 0.4rem;
    text-transform: uppercase;
}

.feature-title {
    color: #C8D8C8;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.feature-desc {
    color: #3A5A3A;
    font-size: 0.82rem;
    font-family: 'JetBrains Mono', monospace;
    line-height: 1.8;
}

/* ─── SECTION HEADER ─────────────────────────────────── */
.section-header {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 1.8rem;
    padding: 0 0.5rem;
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1A3A1A, transparent);
}

.section-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #00FF41;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border: 1px solid #1A3A1A;
    background: rgba(0,255,65,0.03);
}

/* ─── SCROLLBAR ──────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #030703; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #1A3A1A, #0D1F0D);
    border-radius: 0;
}
::-webkit-scrollbar-thumb:hover { background: #00FF41; }

/* ─── MOBILE ─────────────────────────────────────────── */
@media screen and (max-width: 992px) {
    .hero-container {
        flex-direction: column-reverse;
        padding: 2rem 1.5rem;
        text-align: left;
        gap: 2.5rem;
        min-height: auto;
    }

    .hero-content { max-width: 100%; }
    .typing-name { font-size: 3rem; }

    .hero-description {
        font-size: 0.82rem;
        max-width: 100%;
    }

    .profile-frame {
        width: 300px;
        height: 390px;
    }

    .side-panel, .left-panel { display: none; }
}

@media screen and (max-width: 480px) {
    .typing-name { font-size: 2.3rem; }
    .profile-frame { width: 260px; height: 340px; }
    .feature-card { padding: 1.6rem 1.2rem; }
}
</style>
""", unsafe_allow_html=True)

# ── Get profile image ────────────────────────────────────────
profile_img_html = ''
try:
    profile_path = os.path.join("assets", "profiles", "me.jpg")
    if os.path.exists(profile_path):
        img_base64 = get_image_base64(profile_path)
        profile_img_html = f'<img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Robert Macatiag">'
    else:
        profile_img_html = '''
        <div style="
            background: linear-gradient(160deg, #050A05, #0A1A0A, #0F200F);
            width:100%; height:100%;
            display:flex; align-items:center; justify-content:center;
            flex-direction:column; gap:0.8rem;
        ">
            <span style="font-family:Black Ops One,cursive;font-size:4rem;color:#1A3A1A;letter-spacing:4px;">MB</span>
            <span style="font-family:JetBrains Mono,monospace;font-size:0.7rem;color:#00FF41;letter-spacing:4px;">&gt; INITIALIZING</span>
        </div>'''
except:
    profile_img_html = '''
    <div style="
        background:linear-gradient(160deg,#050A05,#0A1A0A);
        width:100%;height:100%;
        display:flex;align-items:center;justify-content:center;
    ">
        <span style="font-family:Black Ops One,cursive;font-size:4rem;color:#1A3A1A;">MB</span>
    </div>'''

# ── HERO HTML ────────────────────────────────────────────────
hero_html = f"""
<div class="hero-container">

    <!-- ═══ LEFT CONTENT ═══ -->
    <div class="hero-content">

        <!-- Status bar -->
        <div class="status-bar">
            <div class="status-dot"></div>
            <span class="status-text">Online</span>
            <span class="status-sep">|</span>
            <span style="color:#333;">SYS:</span>
            <span class="status-id">PORTFOLIO</span>
            <span class="status-sep">|</span>
            <span style="color:#222;">2025</span>
        </div>

        <!-- Greeting prompt -->
        <div class="hero-greeting">
            <span class="prompt-symbol">$</span>
            <span>whoami --user</span>
        </div>

        <!-- Title -->
        <p class="hero-title">Operator Identified</p>

        <!-- Name -->
        <h1 class="typing-name">Robert Macatiag</h1>

        <!-- Accent bar -->
        <div class="name-underline"></div>

        <!-- Role badge -->
        <div class="role-badge">
            <span class="role-text">CS_Student &nbsp;/&nbsp; Developer &nbsp;/&nbsp; Builder</span>
        </div>

        <!-- Description -->
        <p class="hero-description">
            A passionate 3rd-year Computer Science student who turns ideas
            into clean, efficient digital solutions. Fueled by logic,
            creativity, and relentless problem-solving drive.
        </p>

        <!-- Tags -->
        <div class="hero-tags">
            <span class="tag">CS_Student</span>
            <span class="tag">Developer</span>
            <span class="tag">Problem_Solver</span>
            <span class="tag">Builder</span>
        </div>

        <!-- CTA -->
        <div>
            <a href="./About" target="_self" style="text-decoration:none;">
                <button class="cta-button">
                    EXPLORE PORTFOLIO
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
                         stroke="currentColor" stroke-width="3"
                         stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"/>
                        <polyline points="12 5 19 12 12 19"/>
                    </svg>
                </button>
            </a>
        </div>

        <!-- Social Links -->
        <div class="social-links">
            <span class="social-label">LINKS:</span>
            <a href="https://github.com" target="_blank" class="social-icon" title="GitHub">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     stroke="#2A5A2A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61
                             c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77
                             5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0
                             C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78
                             c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                </svg>
            </a>
            <a href="https://linkedin.com" target="_blank" class="social-icon" title="LinkedIn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     stroke="#2A5A2A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                    <rect x="2" y="9" width="4" height="12"/>
                    <circle cx="4" cy="4" r="2"/>
                </svg>
            </a>
            <a href="https://www.facebook.com/" target="_blank" class="social-icon" title="Facebook">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     stroke="#2A5A2A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                </svg>
            </a>
            <a href="./Contact" target="_self" class="social-icon" title="Contact">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     stroke="#2A5A2A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
            </a>
        </div>

    </div>

    <!-- ═══ RIGHT IMAGE ═══ -->
    <div class="hero-image">
        <div class="profile-frame">

            <!-- Outer border -->
            <div class="profile-frame-outer"></div>

            <!-- Corner accents -->
            <div class="corner-tl"></div>
            <div class="corner-tr"></div>
            <div class="corner-bl"></div>
            <div class="corner-br"></div>

            <!-- Main image -->
            <div class="profile-inner">
                {profile_img_html}
            </div>

            <!-- HUD overlay -->
            <div class="hud-overlay">
                <div class="scan-line"></div>
                <div class="hud-bar">
                    <div class="hud-name">// Robert Macatiag</div>
                    <div class="hud-stats">
                        <span class="hud-stat">ROLE: <span>DEV</span></span>
                        <span class="hud-stat">YR: <span>3RD</span></span>
                        <span class="hud-stat">STATUS: <span>ACTIVE</span></span>
                    </div>
                </div>
            </div>

            <!-- Side ticks -->
            <div class="side-panel">
                <div class="side-tick active"></div>
                <div class="side-tick active"></div>
                <div class="side-tick semi"></div>
                <div class="side-tick"></div>
                <div class="side-tick active"></div>
                <div class="side-tick"></div>
                <div class="side-tick semi"></div>
                <div class="side-tick active"></div>
            </div>

            <!-- Left data label -->
            <div class="left-panel">
                <span class="data-block">CS&nbsp;STUDENT</span>
            </div>

        </div>
    </div>

</div>
"""
st.html(hero_html)

# ── FEATURES SECTION ─────────────────────────────────────────
st.markdown("""
<div style="padding: 0 2rem 1rem;">
    <div class="section-header">
        <div class="section-line"></div>
        <div class="section-tag">// Core Modules</div>
        <div class="section-line" style="background:linear-gradient(90deg,transparent,#1A3A1A);"></div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card feature-card-1">
        <div class="feature-num">MODULE_01</div>
        <div class="feature-icon feature-icon-1">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none"
                 stroke="#00FF41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="16 18 22 12 16 6"/>
                <polyline points="8 6 2 12 8 18"/>
            </svg>
        </div>
        <div class="feature-title">Clean Code</div>
        <div class="feature-desc">Writing structured, maintainable code that solves real problems efficiently.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card feature-card-2">
        <div class="feature-num">MODULE_02</div>
        <div class="feature-icon feature-icon-2">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none"
                 stroke="#FF6B00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <line x1="12" y1="8" x2="12" y2="12"/>
                <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
        </div>
        <div class="feature-title">Problem Solving</div>
        <div class="feature-desc">Tackling complex challenges with analytical thinking and creative solutions.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card feature-card-3">
        <div class="feature-num">MODULE_03</div>
        <div class="feature-icon feature-icon-3">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none"
                 stroke="#4A9EFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
            </svg>
        </div>
        <div class="feature-title">Tech Builder</div>
        <div class="feature-desc">Turning concepts into working digital products with modern dev tools.</div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────
st.markdown("""
<style>
.footer {
    background: #030703;
    border-top: 1px solid #1A3A1A;
    padding: 2.5rem 2rem;
    margin-top: 4rem;
    margin-bottom: -5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.footer::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00FF41, #FF6B00, #00FF41, transparent);
    background-size: 200% auto;
    animation: shimmer 4s linear infinite;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.footer-content { max-width: 800px; margin: 0 auto; }

.footer-name {
    font-family: 'Black Ops One', cursive;
    font-size: 1.8rem;
    color: #C8D8C8;
    margin-bottom: 0.3rem;
    letter-spacing: 4px;
    text-shadow: 0 0 30px rgba(0,255,65,0.1);
}

.footer-tagline {
    font-family: 'JetBrains Mono', monospace;
    color: #2A5A2A;
    font-size: 0.8rem;
    margin-bottom: 1.5rem;
    letter-spacing: 2px;
}

.footer-divider {
    width: 80px; height: 2px;
    background: linear-gradient(90deg, #FF6B00, #00FF41);
    margin: 0 auto 1.5rem;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.footer-social {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    margin-bottom: 1.5rem;
}

.footer-social a {
    width: 40px; height: 40px;
    background: rgba(0,0,0,0.5);
    border: 1px solid #1A3A1A;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    text-decoration: none;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
}

.footer-social a:hover {
    border-color: #00FF41;
    box-shadow: 0 0 16px rgba(0,255,65,0.2);
    transform: translateY(-3px);
}

.footer-social a:hover svg { stroke: #00FF41 !important; }

.footer-copyright {
    font-family: 'JetBrains Mono', monospace;
    color: #1E3D1E;
    font-size: 0.78rem;
    letter-spacing: 2px;
}

.footer-heart { color: #FF6B00; }
</style>

<div class="footer">
    <div class="footer-content">
        <h3 class="footer-name">ROBERT MACATIAG</h3>
        <p class="footer-tagline">$ echo "building with passion and code"</p>
        <div class="footer-divider"></div>
        <div class="footer-social">
            <a href="https://github.com" target="_blank">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2A5A2A" stroke-width="2">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61
                             c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77
                             5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0
                             C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78
                             c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                </svg>
            </a>
            <a href="https://linkedin.com" target="_blank">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2A5A2A" stroke-width="2">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                    <rect x="2" y="9" width="4" height="12"/>
                    <circle cx="4" cy="4" r="2"/>
                </svg>
            </a>
            <a href="https://facebook.com" target="_blank">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2A5A2A" stroke-width="2">
                    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                </svg>
            </a>
            <a href="mailto:robertmacatiag@email.com">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2A5A2A" stroke-width="2">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
            </a>
        </div>
        <p class="footer-copyright">
            BUILT WITH <span class="footer-heart">⚡</span> BY ROBERT MACATIAG &copy; 2026
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Render sidebar
render_sidebar()