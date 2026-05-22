import streamlit as st
import streamlit.components.v1 as components
import re
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sidebar import apply_sidebar_styles, render_sidebar

st.set_page_config(
    page_title='Contact | Robert Macatiag',
    page_icon='💻',
    layout='wide'
)

apply_sidebar_styles()

st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Black+Ops+One&display=swap');

/* ─── Reset & Global ─────────────────────────────────── */
* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

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
    padding-left: 2rem !important;
    padding-right: 2rem !important;
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
.contact-header {
    padding: 1rem 0.5rem 2rem;
    position: relative;
    animation: fadeInDown 0.6s ease;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
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

.contact-title {
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

.contact-title span {
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

.contact-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #2A5A2A;
    letter-spacing: 2px;
}

.contact-subtitle::before {
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

/* ─── CONTACT INFO CARD ──────────────────────────────── */
.contact-info {
    background: rgba(5, 12, 5, 0.95);
    border: 1px solid #152515;
    border-top: 3px solid #00FF41;
    padding: 2.2rem;
    position: relative;
    clip-path: polygon(
        0 0,
        calc(100% - 16px) 0,
        100% 16px,
        100% 100%,
        16px 100%,
        0 calc(100% - 16px)
    );
    animation: fadeInLeft 0.6s ease;
}

@keyframes fadeInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
}

/* Corner accent */
.contact-info::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 16px; height: 16px;
    background: #00FF41;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.4;
}

.info-title {
    font-family: 'Barlow Condensed', sans-serif;
    color: #C8D8C8;
    font-size: 1.4rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
}

/* ─── CONTACT ITEM ───────────────────────────────────── */
.contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
    padding: 1rem 1.2rem;
    background: rgba(0,0,0,0.3);
    border: 1px solid #1A3A1A;
    border-left: 3px solid #1E3D1E;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
    clip-path: polygon(
        0 0,
        calc(100% - 10px) 0,
        100% 10px,
        100% 100%,
        10px 100%,
        0 calc(100% - 10px)
    );
}

.contact-item::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 10px; height: 10px;
    background: #1A3A1A;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
}

.contact-item-green  { border-left-color: #00FF41 !important; }
.contact-item-orange { border-left-color: #FF6B00 !important; }
.contact-item-blue   { border-left-color: #4A9EFF !important; }
.contact-item-purple { border-left-color: #DDA0DD !important; }

.contact-item:hover {
    transform: translateX(6px);
    border-color: #2A4A2A;
    background: rgba(0,255,65,0.03);
    box-shadow: 0 4px 20px rgba(0,255,65,0.08);
}

.contact-icon {
    width: 48px; height: 48px;
    background: rgba(0,0,0,0.4);
    border: 1px solid #1E3D1E;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    transition: transform 0.3s ease;
}

.contact-item:hover .contact-icon { transform: scale(1.1); }

.contact-icon-green  { border-color: #00FF41 !important; }
.contact-icon-orange { border-color: #FF6B00 !important; }
.contact-icon-blue   { border-color: #4A9EFF !important; }
.contact-icon-purple { border-color: #DDA0DD !important; }

.contact-text h4 {
    margin: 0 0 0.2rem 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #2A5A2A;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
}

.contact-text p {
    margin: 0;
    font-family: 'JetBrains Mono', monospace;
    color: #C8D8C8;
    font-size: 0.88rem;
    letter-spacing: 0.5px;
}

/* ─── SOCIAL SECTION ─────────────────────────────────── */
.social-section {
    margin-top: 2rem;
}

.social-title {
    font-family: 'JetBrains Mono', monospace;
    color: #2A5A2A;
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.social-title::before {
    content: '//';
    color: #FF6B00;
    font-weight: 800;
}

.social-links {
    display: flex;
    gap: 0.7rem;
    flex-wrap: wrap;
    align-items: center;
}

.social-btn {
    width: 46px; height: 46px;
    background: rgba(0,0,0,0.5);
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

.social-btn:hover {
    border-color: #00FF41;
    box-shadow: 0 0 16px rgba(0,255,65,0.2);
    transform: translateY(-4px);
    background: rgba(0,255,65,0.05);
}

.social-btn:hover svg { stroke: #00FF41 !important; }
.social-btn svg {
    width: 20px; height: 20px;
    stroke: #2A5A2A;
    transition: stroke 0.3s ease;
}

/* ─── CONTACT FORM ───────────────────────────────────── */
.contact-form-wrapper {
    background: rgba(5, 12, 5, 0.95);
    border: 1px solid #152515;
    border-top: 3px solid #FF6B00;
    padding: 2.2rem;
    position: relative;
    clip-path: polygon(
        0 0,
        calc(100% - 16px) 0,
        100% 16px,
        100% 100%,
        16px 100%,
        0 calc(100% - 16px)
    );
    animation: fadeInRight 0.6s ease;
}

@keyframes fadeInRight {
    from { opacity: 0; transform: translateX(20px); }
    to   { opacity: 1; transform: translateX(0); }
}

.contact-form-wrapper::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 16px; height: 16px;
    background: #FF6B00;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.4;
}

.form-title {
    font-family: 'Barlow Condensed', sans-serif;
    color: #C8D8C8;
    font-size: 1.4rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
}

/* ─── FORM INPUTS ────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(0,0,0,0.4) !important;
    border: 1px solid #1E3D1E !important;
    border-radius: 0 !important;
    color: #C8D8C8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88rem !important;
    transition: all 0.3s ease !important;
    caret-color: #00FF41 !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #00FF41 !important;
    box-shadow: 0 0 0 2px rgba(0,255,65,0.1),
                inset 0 0 8px rgba(0,255,65,0.03) !important;
    background: rgba(0,255,65,0.02) !important;
}

.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: #2A4A2A !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.stTextInput label,
.stTextArea label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    color: #2A5A2A !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* Character counter */
.char-counter {
    text-align: right;
    font-size: 0.7rem;
    color: #2A4A2A;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    margin-top: -0.8rem;
    margin-bottom: 0.5rem;
}

.char-counter.warning { color: #FF8C00; }
.char-counter.danger  { color: #FF4444; }

/* Submit button */
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #FF6B00 0%, #CC5500 50%, #AA4400 100%) !important;
    color: #050A05 !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0.85rem 2rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800 !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    cursor: pointer !important;
    clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%, 14px 50%) !important;
    box-shadow: 0 0 0 1px rgba(255,107,0,0.5),
                0 8px 30px rgba(255,107,0,0.25) !important;
}

.stFormSubmitButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 0 0 1px rgba(255,107,0,0.8),
                0 12px 40px rgba(255,107,0,0.4) !important;
}

.stFormSubmitButton > button:active {
    transform: translateY(-1px) !important;
}

/* ─── MAP SECTION ────────────────────────────────────── */
.map-container {
    background: rgba(5, 12, 5, 0.95);
    border: 1px solid #152515;
    border-top: 3px solid #4A9EFF;
    padding: 2rem;
    margin-top: 2rem;
    position: relative;
    overflow: hidden;
    clip-path: polygon(
        0 0,
        calc(100% - 20px) 0,
        100% 20px,
        100% 100%,
        20px 100%,
        0 calc(100% - 20px)
    );
    animation: fadeInUp 0.6s ease;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.map-container::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 20px; height: 20px;
    background: #4A9EFF;
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    opacity: 0.4;
}

.map-title {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-family: 'Barlow Condensed', sans-serif;
    color: #C8D8C8;
    font-size: 1.4rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.map-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #2A5A2A;
    margin-bottom: 1.2rem;
    letter-spacing: 1px;
}

.map-subtitle::before {
    content: '// ';
    color: #FF6B00;
}

.map-embed {
    width: 100%;
    height: 300px;
    border: 1px solid #1E3D1E;
    margin: 0.8rem 0;
    filter: grayscale(0.4) contrast(1.05);
    transition: filter 0.3s ease;
}

.map-embed:hover { filter: grayscale(0) contrast(1.05); }

/* Map action buttons */
.map-action-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1.2rem;
    background: transparent;
    border: 1px solid #1E3D1E;
    color: #2A5A2A;
    text-decoration: none !important;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
    justify-content: center;
    width: 100%;
}

.map-action-btn:hover {
    background: rgba(0,255,65,0.08);
    color: #00FF41 !important;
    border-color: #00FF41;
    box-shadow: 0 0 14px rgba(0,255,65,0.15);
    transform: translateY(-2px);
    text-decoration: none !important;
}

.map-action-btn svg { width: 16px; height: 16px; }

/* ─── COPY BUTTONS (Streamlit) ───────────────────────── */
div[data-testid="stButton"] > button {
    background: transparent !important;
    color: #2A5A2A !important;
    border: 1px solid #1E3D1E !important;
    border-radius: 0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    transition: all 0.25s ease !important;
    clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%) !important;
    padding: 0.4rem 1rem !important;
}

div[data-testid="stButton"] > button:hover {
    background: rgba(0,255,65,0.08) !important;
    color: #00FF41 !important;
    border-color: #00FF41 !important;
    box-shadow: 0 0 12px rgba(0,255,65,0.15) !important;
    transform: translateY(-2px) !important;
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
    0%   { background-position: 0% center; }
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
@media screen and (max-width: 768px) {
    .contact-title { font-size: 2.5rem; }
    .contact-info, .contact-form-wrapper { padding: 1.6rem; }
    .map-embed { height: 240px; }
}

@media screen and (max-width: 480px) {
    .contact-title { font-size: 2rem; }
    .social-btn { width: 40px; height: 40px; }
    .social-btn svg { width: 18px; height: 18px; }
    .map-embed { height: 200px; }
}
</style>
''', unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────────────────
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'submit_message' not in st.session_state:
    st.session_state.submit_message = ''

# ── Page Header ───────────────────────────────────────────────────────────────
st.markdown('''
<div class="contact-header">
    <div class="page-header-badge">ping --target contact</div>
    <h1 class="contact-title">Get In <span>Touch</span></h1>
    <div class="title-underline"></div>
    <p class="contact-subtitle">
        open to opportunities — let's build something together
    </p>
</div>
''', unsafe_allow_html=True)

# ── Section divider ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// Establish Connection</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

# ── Two-column layout ─────────────────────────────────────────────────────────
contact_info_col, contact_form_col = st.columns(2, gap="large")

# ══ LEFT: Contact Info ════════════════════════════════════════════════════════
with contact_info_col:

    st.markdown('''
    <div class="contact-info">
        <h2 class="info-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#00FF41" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2
                         19.79 19.79 0 0 1-8.63-3.07
                         19.5 19.5 0 0 1-6-6
                         19.79 19.79 0 0 1-3.07-8.67
                         A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72
                         12.84 12.84 0 0 0 .7 2.81
                         2 2 0 0 1-.45 2.11L8.09 9.91
                         a16 16 0 0 0 6 6l1.27-1.27
                         a2 2 0 0 1 2.11-.45
                         12.84 12.84 0 0 0 2.81.7
                         A2 2 0 0 1 22 16.92z"/>
            </svg>
            Contact Information
        </h2>
    </div>
    ''', unsafe_allow_html=True)

    # Location
    st.markdown('''
    <div class="contact-item contact-item-green">
        <div class="contact-icon contact-icon-green">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#00FF41" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                <circle cx="12" cy="10" r="3"/>
            </svg>
        </div>
        <div class="contact-text">
            <h4>Location</h4>
            <p>Luy-a, Aroroy, Masbate</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    if st.button("📋 COPY_LOCATION", key="copy_location",
                 use_container_width=True):
        st.code("Luy-a, Aroroy, Masbate", language=None)
        st.success("✅ Location copied to clipboard!")

    st.markdown('<div style="margin-bottom:0.8rem;"></div>',
                unsafe_allow_html=True)

    # Email
    st.markdown('''
    <div class="contact-item contact-item-orange">
        <div class="contact-icon contact-icon-orange">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#FF6B00" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2
                         H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
            </svg>
        </div>
        <div class="contact-text">
            <h4>Email</h4>
            <p>robertmacatiag@email.com</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    if st.button("📋 COPY_EMAIL", key="copy_email",
                 use_container_width=True):
        st.code("robertmacatiag@email.com", language=None)
        st.success("✅ Email copied to clipboard!")

    st.markdown('<div style="margin-bottom:0.8rem;"></div>',
                unsafe_allow_html=True)

    # Phone
    st.markdown('''
    <div class="contact-item contact-item-blue">
        <div class="contact-icon contact-icon-blue">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#4A9EFF" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2
                         19.79 19.79 0 0 1-8.63-3.07
                         19.5 19.5 0 0 1-6-6
                         19.79 19.79 0 0 1-3.07-8.67
                         A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72
                         12.84 12.84 0 0 0 .7 2.81
                         2 2 0 0 1-.45 2.11L8.09 9.91
                         a16 16 0 0 0 6 6l1.27-1.27
                         a2 2 0 0 1 2.11-.45
                         12.84 12.84 0 0 0 2.81.7
                         A2 2 0 0 1 22 16.92z"/>
            </svg>
        </div>
        <div class="contact-text">
            <h4>Phone</h4>
            <p>+63 912 345 6789</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    if st.button("📋 COPY_PHONE", key="copy_phone",
                 use_container_width=True):
        st.code("+63 912 345 6789", language=None)
        st.success("✅ Phone copied to clipboard!")

    st.markdown('<div style="margin-bottom:0.8rem;"></div>',
                unsafe_allow_html=True)

    # University
    st.markdown('''
    <div class="contact-item contact-item-purple">
        <div class="contact-icon contact-icon-purple">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#DDA0DD" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                <path d="M6 12v5c3 3 9 3 12 0v-5"/>
            </svg>
        </div>
        <div class="contact-text">
            <h4>University</h4>
            <p>3rd Year Computer Science Student</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div style="margin-top:1.8rem;"></div>',
                unsafe_allow_html=True)

    # Social Links
    st.markdown('''
    <div class="social-section">
        <div class="social-title">Connect With Me</div>
        <div class="social-links">
            <a href="https://github.com" target="_blank"
               class="social-btn" title="GitHub">
                <svg viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                    <path d="M9 19c-5 1.5-5-2.5-7-3
                             m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61
                             c3.14-.35 6.44-1.54 6.44-7
                             A5.44 5.44 0 0 0 20 4.77
                             5.07 5.07 0 0 0 19.91 1
                             S18.73.65 16 2.48
                             a13.38 13.38 0 0 0-7 0
                             C6.27.65 5.09 1 5.09 1
                             A5.07 5.07 0 0 0 5 4.77
                             a5.44 5.44 0 0 0-1.5 3.78
                             c0 5.42 3.3 6.61 6.44 7
                             A3.37 3.37 0 0 0 9 18.13V22"/>
                </svg>
            </a>
            <a href="https://linkedin.com" target="_blank"
               class="social-btn" title="LinkedIn">
                <svg viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7
                             a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7
                             a6 6 0 0 1 6-6z"/>
                    <rect x="2" y="9" width="4" height="12"/>
                    <circle cx="4" cy="4" r="2"/>
                </svg>
            </a>
            <a href="https://www.facebook.com/Missbea070322"
               target="_blank" class="social-btn" title="Facebook">
                <svg viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                </svg>
            </a>
            <a href="https://twitter.com" target="_blank"
               class="social-btn" title="Twitter">
                <svg viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                    <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53
                             4.48 4.48 0 0 0-7.86 3v1
                             A10.66 10.66 0 0 1 3 4s-4 9 5 13
                             a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5
                             a4.5 4.5 0 0 0-.08-.83
                             A7.72 7.72 0 0 0 23 3z"/>
                </svg>
            </a>
            <a href="https://instagram.com" target="_blank"
               class="social-btn" title="Instagram">
                <svg viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                    <rect x="2" y="2" width="20" height="20"
                          rx="5" ry="5"/>
                    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
                    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
                </svg>
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# ══ RIGHT: Contact Form ═══════════════════════════════════════════════════════
with contact_form_col:

    st.markdown('''
    <div class="contact-form-wrapper">
        <h2 class="form-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                 stroke="#FF6B00" stroke-width="2"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5
                         a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            Send A Message
        </h2>
    </div>
    ''', unsafe_allow_html=True)

    with st.form('contact_form', clear_on_submit=True):
        name    = st.text_input(
            'Your Name',
            placeholder='Enter your name',
            max_chars=50
        )
        email   = st.text_input(
            'Your Email',
            placeholder='Enter your email',
            max_chars=100
        )
        subject = st.text_input(
            'Subject',
            placeholder='What is this about?',
            max_chars=100
        )
        message = st.text_area(
            'Message',
            placeholder='Tell me something...',
            height=150,
            max_chars=500
        )

        if message:
            char_count    = len(message)
            counter_class = (
                'danger'  if char_count > 450 else
                'warning' if char_count > 400 else ''
            )
            st.markdown(
                f'<div class="char-counter {counter_class}">'
                f'{char_count}/500 characters</div>',
                unsafe_allow_html=True
            )

        submit = st.form_submit_button('▶ TRANSMIT MESSAGE')

        if submit:
            if not name or not email or not subject or not message:
                st.error('⚠ All fields required — fill in missing data.')
            elif not re.match(
                r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                email
            ):
                st.error('⚠ Invalid email address — check your input.')
            else:
                with st.spinner('Transmitting message...'):
                    time.sleep(1.5)
                st.session_state.form_submitted = True
                st.session_state.submit_message = (
                    f'✅ Message received, {name}! '
                    f'Transmission successful. Standing by for response.'
                )
                st.success(st.session_state.submit_message)

# ── Map Section ───────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">
    <div class="section-line"></div>
    <div class="section-tag">// GPS Coordinates</div>
    <div class="section-line-rev"></div>
</div>
""", unsafe_allow_html=True)

st.markdown('''
<div class="map-container">
    <h2 class="map-title">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
             stroke="#4A9EFF" stroke-width="2"
             stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
        </svg>
        Find Me Here
    </h2>
    <p class="map-subtitle">Luy-a, Aroroy, Masbate, Philippines</p>
</div>
''', unsafe_allow_html=True)

map_html = '''
<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.5!2d123.6!3d12.4!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTLCsDI0JzAwLjAiTiAxMjPCsDM2JzAwLjAiRQ!5e0!3m2!1sen!2sph!4v1234567890"
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="Location Map"
    style="
        width: 100%;
        height: 300px;
        border: 1px solid #1E3D1E;
        filter: grayscale(0.5) contrast(1.05) brightness(0.85);
        display: block;
    ">
</iframe>
'''
components.html(map_html, height=320)

# Map action buttons
map_col1, map_col2 = st.columns(2)
with map_col1:
    st.markdown('''
    <a href="https://www.google.com/maps/search/?api=1&query=Luy-A+Aroroy+Masbate+Philippines"
       target="_blank" class="map-action-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
            <polyline points="15 3 21 3 21 9"/>
            <line x1="10" y1="14" x2="21" y2="3"/>
        </svg>
        Open in Google Maps
    </a>
    ''', unsafe_allow_html=True)

with map_col2:
    st.markdown('''
    <a href="https://maps.apple.com/?q=Bugtong,Mandaon,Masbate"
       target="_blank" class="map-action-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 2a10 10 0 0 1 10 10"/>
        </svg>
        Open in Apple Maps
    </a>
    ''', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <h3 class="footer-name">ROBERT MACATIAG</h3>
        <p class="footer-tagline">
            $ echo "let's create something amazing together"
        </p>
        <div class="footer-divider"></div>
        <p class="footer-copyright">
            BUILT WITH <span class="footer-heart">⚡</span>
            BY ROBERT MACATIAG &copy; 2026
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

render_sidebar()