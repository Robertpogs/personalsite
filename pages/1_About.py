import streamlit as st
import os
import base64
import sys
from PIL import Image
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sidebar import apply_sidebar_styles, render_sidebar

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(
    page_title="About | Robert Macatiag",
    page_icon="💻",
    layout="wide"
)

apply_sidebar_styles()

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
    padding-top: 1.5rem !important;
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

/* ─── SCROLLBAR ──────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #030703; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #1A3A1A, #0D1F0D);
    border-radius: 0;
}
::-webkit-scrollbar-thumb:hover { background: #00FF41; }

/* ─── PAGE HEADER ────────────────────────────────────── */
.page-header {
    padding: 1rem 0.5rem 2.5rem;
    position: relative;
}

.page-header-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00FF41;
    padding: 0.4rem 1rem;
    border: 1px solid #1A3A1A;
    background: rgba(0,255,65,0.03);
    margin-bottom: 1rem;
    clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
}

.page-header-badge::before {
    content: '$';
    color: #FF6B00;
    font-weight: 800;
}

.page-main-title {
    font-family: 'Black Ops One', cursive;
    font-size: 3.5rem;
    font-weight: 400;
    color: #E8F5E9;
    margin-bottom: 0.3rem;
    line-height: 1.1;
    letter-spacing: 3px;
    text-shadow:
        0 0 40px rgba(0, 255, 65, 0.15),
        2px 2px 0px #1A2A1A,
        4px 4px 0px #0D180D;
}

.page-main-title span {
    color: #00FF41;
    text-shadow:
        0 0 20px rgba(0,255,65,0.4),
        2px 2px 0px #0A1A0A;
}

.title-underline {
    width: 200px;
    height: 4px;
    background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 30%, #00FF41 60%, transparent 100%);
    margin-bottom: 1rem;
    clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
}

.page-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #2A5A2A;
    letter-spacing: 2px;
}

.page-subtitle::before {
    content: '// ';
    color: #FF6B00;
}

/* ─── SECTION HEADER ─────────────────────────────────── */
.section-header {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 2rem;
    padding: 0 0.5rem;
}

.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1A3A1A, transparent);
}

.section-line-rev {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1A3A1A);
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
    white-space: nowrap;
}

/* ─── ABOUT CONTAINER ────────────────────────────────── */
.about-container {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 5rem;
    padding: 0 1rem 3rem;
    position: relative;
}

.about-container::before {
    content: '';
    position: absolute;
    top: 20px; left: 20px;
    width: 60px; height: 60px;
    border-top: 3px solid #00FF41;
    border-left: 3px solid #00FF41;
    opacity: 0.3;
    pointer-events: none;
}

.about-container::after {
    content: '';
    position: absolute;
    bottom: 20px; right: 20px;
    width: 60px; height: 60px;
    border-bottom: 3px solid #FF6B00;
    border-right: 3px solid #FF6B00;
    opacity: 0.3;
    pointer-events: none;
}

/* ─── IMAGE SECTION ──────────────────────────────────── */
.about-image-section {
    flex: 0 0 340px;
    position: relative;
}

.profile-frame {
    position: relative;
    width: 340px;
    height: 440px;
}

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

.corner-tl, .corner-tr, .corner-bl, .corner-br {
    position: absolute;
    width: 30px; height: 30px;
    z-index: 3;
}

.corner-tl {
    top: -2px; left: -2px;
    border-top: 3px solid #00FF41;
    border-left: 3px solid #00FF41;
    box-shadow: -3px -3px 12px rgba(0,255,65,0.4);
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
    object-position: center top;
    display: block;
    filter: contrast(1.05) saturate(0.85);
}

/* HUD overlay */
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

.hud-stat span { color: #FF6B00; }

/* Side ticks */
.side-panel {
    position: absolute;
    right: -46px;
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
}

.side-tick.active {
    background: #00FF41;
    box-shadow: 0 0 6px #00FF41;
}

.side-tick.semi {
    background: #FF6B00;
    width: 18px;
}

/* ─── ABOUT CONTENT ──────────────────────────────────── */
.about-content {
    flex: 1;
    position: relative;
    z-index: 1;
}

.status-bar {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1.2rem;
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

.status-text { color: #00FF41; text-transform: uppercase; letter-spacing: 3px; }
.status-sep { color: #333; }
.status-id { color: #FF6B00; font-weight: 600; }

.about-name {
    font-family: 'Black Ops One', cursive;
    font-size: 2.8rem;
    font-weight: 400;
    color: #E8F5E9;
    margin-bottom: 0.4rem;
    line-height: 1.1;
    letter-spacing: 3px;
    text-shadow:
        0 0 30px rgba(0,255,65,0.15),
        2px 2px 0px #1A2A1A;
}

.about-name span { color: #00FF41; }

.name-underline {
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 30%, #00FF41 60%, transparent 100%);
    margin-bottom: 1.2rem;
    clip-path: polygon(0 0, calc(100% - 12px) 0, 100% 100%, 12px 100%);
}

.role-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(255, 107, 0, 0.08);
    border: 1px solid rgba(255, 107, 0, 0.3);
    border-left: 4px solid #FF6B00;
    padding: 0.5rem 1.2rem;
    margin-bottom: 1.8rem;
    clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 50%, calc(100% - 10px) 100%, 0 100%);
}

.role-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #FF8C00;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
}

.about-description {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.86rem;
    color: #4A7A4A;
    line-height: 2;
    margin-bottom: 2rem;
    padding: 1.4rem 1.6rem;
    background: rgba(0,255,65,0.02);
    border: 1px solid #1A2E1A;
    border-left: 3px solid #2A4A2A;
    position: relative;
}

.about-description::before {
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

/* ─── INFO CARDS ─────────────────────────────────────── */
.info-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1.5rem;
}

.info-card {
    background: rgba(5, 12, 5, 0.95);
    padding: 1.2rem 1.4rem;
    border: 1px solid #152515;
    border-left: 3px solid #1E3D1E;
    display: flex;
    align-items: center;
    gap: 1rem;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
    clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 10px 100%, 0 calc(100% - 10px));
}

.info-card::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 10px; height: 10px;
    background: #1A3A1A;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
}

.info-card-1 { border-left-color: #00FF41; }
.info-card-2 { border-left-color: #FF6B00; }
.info-card-3 { border-left-color: #4A9EFF; }
.info-card-4 { border-left-color: #DDA0DD; }

.info-card:hover {
    transform: translateY(-4px) translateX(2px);
    border-color: #2A4A2A;
}

.info-card-1:hover { box-shadow: 0 8px 30px rgba(0,255,65,0.1), 0 0 0 1px rgba(0,255,65,0.1); }
.info-card-2:hover { box-shadow: 0 8px 30px rgba(255,107,0,0.1), 0 0 0 1px rgba(255,107,0,0.1); }
.info-card-3:hover { box-shadow: 0 8px 30px rgba(74,158,255,0.1), 0 0 0 1px rgba(74,158,255,0.1); }
.info-card-4:hover { box-shadow: 0 8px 30px rgba(221,160,221,0.1), 0 0 0 1px rgba(221,160,221,0.1); }

.info-icon {
    width: 48px; height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    background: rgba(0,0,0,0.4);
    border: 1px solid;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    transition: transform 0.3s ease;
}

.info-card:hover .info-icon { transform: scale(1.08); }

.info-icon-1 { border-color: #00FF41; }
.info-icon-2 { border-color: #FF6B00; }
.info-icon-3 { border-color: #4A9EFF; }
.info-icon-4 { border-color: #DDA0DD; }

.info-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 600;
    color: #2A5A2A;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 0 0 0.25rem 0;
}

.info-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: #C8D8C8;
    font-weight: 600;
    margin: 0;
    letter-spacing: 0.5px;
}

/* ─── SKILL CARDS ────────────────────────────────────── */
.skill-card {
    background: rgba(5, 12, 5, 0.95);
    padding: 2rem 1.8rem;
    border: 1px solid #152515;
    border-top: 3px solid;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
    height: 100%;
    clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 14px, 100% 100%, 14px 100%, 0 calc(100% - 14px));
}

.skill-card::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 14px; height: 14px;
    background: #00FF41;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.3;
    transition: opacity 0.3s ease;
}

.skill-card:hover::after { opacity: 0.8; }

.skill-card-1 { border-top-color: #00FF41; }
.skill-card-2 { border-top-color: #FF6B00; }
.skill-card-3 { border-top-color: #4A9EFF; }

.skill-card:hover {
    transform: translateY(-6px);
    border-color: #2A4A2A;
}

.skill-card-1:hover { box-shadow: 0 12px 40px rgba(0,255,65,0.1), 0 0 0 1px rgba(0,255,65,0.15); }
.skill-card-2:hover { box-shadow: 0 12px 40px rgba(255,107,0,0.1), 0 0 0 1px rgba(255,107,0,0.15); }
.skill-card-3:hover { box-shadow: 0 12px 40px rgba(74,158,255,0.1), 0 0 0 1px rgba(74,158,255,0.15); }

.skill-card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.4rem;
}

.skill-card-icon {
    width: 48px; height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0,0,0,0.4);
    border: 1px solid;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    transition: transform 0.3s ease;
    flex-shrink: 0;
}

.skill-card:hover .skill-card-icon { transform: scale(1.08); }

.skill-icon-1 { border-color: #00FF41; }
.skill-icon-2 { border-color: #FF6B00; }
.skill-icon-3 { border-color: #4A9EFF; }

.skill-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #333;
    letter-spacing: 2px;
    margin-bottom: 0.3rem;
    text-transform: uppercase;
}

.skill-card-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: #C8D8C8;
    margin: 0;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
}

.skill-tag {
    background: transparent;
    color: #00FF41;
    padding: 0.4rem 0.9rem;
    font-size: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    border: 1px solid #1E3D1E;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.25s ease;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    cursor: default;
}

.skill-tag::before {
    content: '#';
    color: #FF6B00;
    margin-right: 3px;
}

.skill-tag:hover {
    background: rgba(0,255,65,0.08);
    border-color: #00FF41;
    box-shadow: 0 0 12px rgba(0,255,65,0.15);
    transform: translateY(-2px);
}

/* ─── FOOTER ─────────────────────────────────────────── */
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

.footer-copyright {
    font-family: 'JetBrains Mono', monospace;
    color: #1E3D1E;
    font-size: 0.78rem;
    letter-spacing: 2px;
}

.footer-heart { color: #FF6B00; }

/* ─── MOBILE ─────────────────────────────────────────── */
@media screen and (max-width: 992px) {
    .about-container {
        flex-direction: column;
        padding: 1rem;
        gap: 2.5rem;
    }

    .about-image-section {
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
    }

    .profile-frame {
        width: 100%;
        height: 380px;
    }

    .side-panel { display: none; }

    .about-name { font-size: 2.2rem; }
    .page-main-title { font-size: 2.5rem; }
    .info-cards { grid-template-columns: 1fr; }
}

@media screen and (max-width: 480px) {
    .about-name { font-size: 1.8rem; }
    .page-main-title { font-size: 2rem; }
    .info-cards { gap: 0.8rem; }
    .info-card { padding: 1rem 1.2rem; }
}
</style>
""", unsafe_allow_html=True)

# ── Page Header ──────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-badge">whoami --verbose</div>
    <h1 class="page-main-title">About <span>Me</span></h1>
    <div class="title-underline"></div>
    <p class="page-subtitle">get to know the operator behind the code</p>
</div>
""", unsafe_allow_html=True)

# ── Section divider ──────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// Operator Profile</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

# ── Get profile image ────────────────────────────────────────
about_img_html = ''
try:
    about_img_path = os.path.join("assets", "profiles", "me.jpg")
    if os.path.exists(about_img_path):
        img_base64 = get_image_base64(about_img_path)
        about_img_html = f'<img src="data:image/jpeg;base64,{img_base64}" class="profile-img" alt="Robert Macatiag">'
    else:
        about_img_html = '''
        <div style="
            background: linear-gradient(160deg, #050A05, #0A1A0A, #0F200F);
            width:100%; height:100%;
            display:flex; align-items:center; justify-content:center;
            flex-direction:column; gap:0.8rem;
        ">
            <span style="font-family:Black Ops One,cursive;font-size:4rem;color:#1A3A1A;letter-spacing:4px;">RM</span>
            <span style="font-family:JetBrains Mono,monospace;font-size:0.7rem;color:#00FF41;letter-spacing:4px;">&gt; INITIALIZING</span>
        </div>'''
except:
    about_img_html = '''
    <div style="
        background:linear-gradient(160deg,#050A05,#0A1A0A);
        width:100%;height:100%;
        display:flex;align-items:center;justify-content:center;
    ">
        <span style="font-family:Black Ops One,cursive;font-size:4rem;color:#1A3A1A;">RM</span>
    </div>'''

# ── About HTML ───────────────────────────────────────────────
about_html = f"""
<div class="about-container">

    <!-- ═══ LEFT: IMAGE ═══ -->
    <div class="about-image-section">
        <div class="profile-frame">

            <div class="profile-frame-outer"></div>

            <div class="corner-tl"></div>
            <div class="corner-tr"></div>
            <div class="corner-bl"></div>
            <div class="corner-br"></div>

            <div class="profile-inner">
                {about_img_html}
            </div>

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

        </div>
    </div>

    <!-- ═══ RIGHT: CONTENT ═══ -->
    <div class="about-content">

        <div class="status-bar">
            <div class="status-dot"></div>
            <span class="status-text">Online</span>
            <span class="status-sep">|</span>
            <span style="color:#333;">ID:</span>
            <span class="status-id">ROBERT_MACATIAG</span>
            <span class="status-sep">|</span>
            <span style="color:#222;">CS_STUDENT</span>
        </div>

        <h2 class="about-name">Robert <span>Macatiag</span></h2>
        <div class="name-underline"></div>

        <div class="role-badge">
            <span class="role-text">3rd Year CS Student &nbsp;/&nbsp; Developer &nbsp;/&nbsp; Builder</span>
        </div>

       <p class="about-description">
            Hey! I'm Robert Macatiag, a third-year Computer Science student driven 
            by the thrill of turning complex logic into clean, functional applications. 
            For me, CS isn't just about writing lines of code; it's about engineering 
            digital environments where design and performance meet.
            <br><br>
            My journey in development has moved from exploring the fundamentals to 
            architecting full-stack solutions. I love the challenge of bridging the gap 
            between intuitive user interfaces and secure, scalable backend systems. If there's 
            a tool or framework that can optimize a project, you can bet I'm already experimenting with it.
            <br><br>
            When I'm away from my code editor, I’m usually diving into tech blogs, 
            discovering modern design trends, or brainstorming features for my next building phase.
        </p>

        <div class="info-cards">
            <div class="info-card info-card-1">
                <div class="info-icon info-icon-1">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                         stroke="#00FF41" stroke-width="2"
                         stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                    </svg>
                </div>
                <div>
                    <p class="info-label">Education</p>
                    <p class="info-value">BS Computer Science · 3rd Year</p>
                </div>
            </div>
            <div class="info-card info-card-2">
                <div class="info-icon info-icon-2">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                         stroke="#FF6B00" stroke-width="2"
                         stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                        <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
                    </svg>
                </div>
                <div>
                    <p class="info-label">Field</p>
                    <p class="info-value">Software Development</p>
                </div>
            </div>
            <div class="info-card info-card-3">
                <div class="info-icon info-icon-3">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                         stroke="#4A9EFF" stroke-width="2"
                         stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 6v6l4 2"/>
                    </svg>
                </div>
                <div>
                    <p class="info-label">Experience</p>
                    <p class="info-value">3+ Years Learning</p>
                </div>
            </div>
            <div class="info-card info-card-4">
                <div class="info-icon info-icon-4">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                         stroke="#DDA0DD" stroke-width="2"
                         stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                        <circle cx="12" cy="10" r="3"/>
                    </svg>
                </div>
                <div>
                    <p class="info-label">Location</p>
                    <p class="info-value">Luy-a, Aroroy, Masbate</p>
                </div>
            </div>
        </div>

    </div>
</div>
"""
st.html(about_html)

# ── Skills Section ───────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// Skill Modules</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

skills_col1, skills_col2, skills_col3 = st.columns(3, gap="medium")

with skills_col1:
    st.markdown("""
    <div class="skill-card skill-card-1">
        <div class="skill-num">MODULE_01</div>
        <div class="skill-card-header">
            <div class="skill-card-icon skill-icon-1">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="#00FF41" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="16 18 22 12 16 6"/>
                    <polyline points="8 6 2 12 8 18"/>
                </svg>
            </div>
            <h4 class="skill-card-title">Programming</h4>
        </div>
        <div class="skill-tags">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Java</span>
            <span class="skill-tag">C++</span>
            <span class="skill-tag">JavaScript</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with skills_col2:
    st.markdown("""
    <div class="skill-card skill-card-2">
        <div class="skill-num">MODULE_02</div>
        <div class="skill-card-header">
            <div class="skill-card-icon skill-icon-2">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="#FF6B00" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                    <line x1="3" y1="9" x2="21" y2="9"/>
                    <line x1="9" y1="21" x2="9" y2="9"/>
                </svg>
            </div>
            <h4 class="skill-card-title">Web Development</h4>
        </div>
        <div class="skill-tags">
            <span class="skill-tag">HTML/CSS</span>
            <span class="skill-tag">Streamlit</span>
            <span class="skill-tag">React</span>
            <span class="skill-tag">Flask</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with skills_col3:
    st.markdown("""
    <div class="skill-card skill-card-3">
        <div class="skill-num">MODULE_03</div>
        <div class="skill-card-header">
            <div class="skill-card-icon skill-icon-3">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="#4A9EFF" stroke-width="2"
                     stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="18" cy="18" r="3"/>
                    <circle cx="6" cy="6" r="3"/>
                    <path d="M13 6h3a2 2 0 0 1 2 2v7"/>
                    <line x1="6" y1="9" x2="6" y2="21"/>
                </svg>
            </div>
            <h4 class="skill-card-title">Tools & Others</h4>
        </div>
        <div class="skill-tags">
            <span class="skill-tag">Git</span>
            <span class="skill-tag">VS Code</span>
            <span class="skill-tag">MySQL</span>
            <span class="skill-tag">Figma</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <h3 class="footer-name">ROBERT MACATIAG</h3>
        <p class="footer-tagline">$ echo "building with passion and code"</p>
        <div class="footer-divider"></div>
        <p class="footer-copyright">
            BUILT WITH <span class="footer-heart">⚡</span> BY ROBERT MACATIAG &copy; 2026
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

render_sidebar()