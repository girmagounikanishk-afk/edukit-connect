import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="EduKit Connect — Learn it. Build it. See it.",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}
[data-testid="collapsedControl"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important; margin: 0 !important;}
.stApp {margin: 0; padding: 0;}
iframe {border: none; display: block;}
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EduKit Connect — Learn it. Build it. See it.</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Fredoka:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --coral:#FF6B6B;--coral-light:#FFE8E8;--coral-dark:#E84545;
  --teal:#00C9A7;--teal-light:#E0FBF5;--teal-dark:#00957A;
  --purple:#A855F7;--purple-light:#F3E8FF;--purple-dark:#7C3AED;
  --orange:#FF9500;--orange-light:#FFF3E0;--orange-dark:#E67E00;
  --yellow:#FFD60A;--yellow-light:#FFFDE7;
  --navy:#1A1A2E;--navy2:#16213E;--navy3:#0F3460;
  --cream:#FAFAF7;--white:#FFFFFF;
  --text-dark:#1A1A2E;--text-mid:#4A5568;--text-soft:#718096;
  --border:#E8E8F0;
  --r-sm:8px;--r-md:16px;--r-lg:24px;--r-xl:32px;--r-full:999px;
  --shadow-sm:0 2px 8px rgba(0,0,0,0.06);
  --shadow-md:0 8px 32px rgba(0,0,0,0.1);
  --shadow-lg:0 20px 60px rgba(0,0,0,0.15);
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Nunito',sans-serif;background:var(--cream);color:var(--text-dark);overflow-x:hidden;}
h1,h2,h3,h4,.brand{font-family:'Fredoka',sans-serif;}

/* ── NAV ── */
nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(255,255,255,0.92);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);transition:box-shadow .3s;}
nav.scrolled{box-shadow:var(--shadow-md);}
.nav-inner{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:8px;}
.nav-logo{font-family:'Fredoka',sans-serif;font-size:22px;font-weight:700;color:var(--coral);cursor:pointer;margin-right:16px;display:flex;align-items:center;gap:8px;white-space:nowrap;}
.nav-logo span{color:var(--teal);}
.nav-links{display:flex;gap:4px;flex:1;overflow-x:auto;}
.nav-link{padding:8px 12px;font-size:13px;font-weight:600;color:var(--text-mid);cursor:pointer;border-radius:var(--r-full);transition:all .2s;white-space:nowrap;border:none;background:none;}
.nav-link:hover,.nav-link.active{background:var(--coral-light);color:var(--coral);}
.nav-cta{margin-left:auto;background:var(--coral);color:#fff;border:none;border-radius:var(--r-full);padding:10px 20px;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap;transition:all .2s;font-family:'Nunito',sans-serif;}
.nav-cta:hover{background:var(--coral-dark);transform:translateY(-1px);}

/* ── PAGES ── */
.page{display:none;min-height:100vh;padding-top:64px;}
.page.active{display:block;}

/* ── HERO ── */
.hero{
  min-height:calc(100vh - 64px);
  background:linear-gradient(135deg,var(--navy) 0%,var(--navy3) 50%,#1B4F72 100%);
  position:relative;overflow:hidden;
  display:flex;align-items:center;
}
.hero-canvas{position:absolute;inset:0;z-index:0;}
.hero-content{position:relative;z-index:2;max-width:1200px;margin:0 auto;padding:60px 24px;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;}
.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:var(--r-full);padding:6px 16px;font-size:13px;color:rgba(255,255,255,0.8);margin-bottom:24px;}
.hero-eyebrow span{width:6px;height:6px;background:var(--teal);border-radius:50%;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.5;transform:scale(1.5);}}
.hero h1{font-size:clamp(2.2rem,5vw,3.6rem);font-weight:700;color:#fff;line-height:1.1;margin-bottom:20px;}
.hero h1 em{font-style:normal;color:var(--yellow);}
.hero h1 strong{font-style:normal;color:var(--teal);}
.hero-sub{font-size:16px;color:rgba(255,255,255,0.7);line-height:1.6;margin-bottom:32px;max-width:480px;}
.hero-btns{display:flex;gap:12px;flex-wrap:wrap;}
.btn-primary{background:var(--coral);color:#fff;border:none;border-radius:var(--r-full);padding:14px 28px;font-size:15px;font-weight:700;cursor:pointer;transition:all .25s;font-family:'Nunito',sans-serif;display:inline-flex;align-items:center;gap:8px;}
.btn-primary:hover{background:var(--coral-dark);transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,107,107,0.4);}
.btn-outline{background:transparent;color:#fff;border:2px solid rgba(255,255,255,0.3);border-radius:var(--r-full);padding:14px 28px;font-size:15px;font-weight:700;cursor:pointer;transition:all .25s;font-family:'Nunito',sans-serif;}
.btn-outline:hover{border-color:#fff;background:rgba(255,255,255,0.1);}
.hero-stats{display:flex;gap:32px;margin-top:40px;}
.hstat{text-align:left;}
.hstat-num{font-family:'Fredoka',sans-serif;font-size:2rem;font-weight:600;color:var(--yellow);}
.hstat-label{font-size:12px;color:rgba(255,255,255,0.6);margin-top:2px;}
.hero-visual{display:flex;justify-content:center;align-items:center;}
.hero-orb{width:380px;height:380px;position:relative;}
.hero-orb canvas{position:absolute;inset:0;}

/* floating shapes */
.float-shape{position:absolute;border-radius:var(--r-xl);animation:floatUp 6s ease-in-out infinite;}
@keyframes floatUp{0%,100%{transform:translateY(0) rotate(0deg);}50%{transform:translateY(-20px) rotate(5deg);}}

/* ── SECTIONS ── */
.section{padding:80px 24px;}
.section-inner{max-width:1200px;margin:0 auto;}
.section-label{display:inline-block;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--coral);margin-bottom:12px;}
.section-title{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:700;color:var(--text-dark);line-height:1.2;margin-bottom:16px;}
.section-title em{font-style:normal;color:var(--coral);}
.section-sub{font-size:16px;color:var(--text-soft);max-width:560px;line-height:1.6;}

/* ── ABOUT STRIP ── */
.about-strip{background:var(--white);padding:48px 24px;}
.about-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1.5fr;gap:60px;align-items:center;}
.about-badge{width:72px;height:72px;border-radius:var(--r-lg);background:linear-gradient(135deg,var(--coral),var(--purple));display:flex;align-items:center;justify-content:center;font-size:2rem;margin-bottom:20px;}
.about-title{font-size:1.8rem;font-weight:700;color:var(--text-dark);margin-bottom:12px;}
.about-body{font-size:15px;color:var(--text-soft);line-height:1.7;}
.about-right{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.about-card{background:var(--cream);border-radius:var(--r-lg);padding:20px;border:2px solid transparent;transition:all .25s;cursor:default;}
.about-card:hover{border-color:var(--coral);transform:translateY(-4px);}
.about-card-icon{font-size:2rem;margin-bottom:10px;}
.about-card-title{font-size:14px;font-weight:700;color:var(--text-dark);margin-bottom:4px;}
.about-card-text{font-size:13px;color:var(--text-soft);line-height:1.5;}

/* ── PRODUCT GRID ── */
.products-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;margin-top:40px;}
.product-card{
  background:var(--white);border-radius:var(--r-xl);overflow:hidden;
  box-shadow:var(--shadow-sm);border:1px solid var(--border);
  transition:all .3s;cursor:pointer;position:relative;
}
.product-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:transparent;}
.product-thumb{height:200px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;}
.product-thumb canvas{position:absolute;inset:0;}
.product-emoji-bg{position:relative;z-index:1;font-size:4rem;filter:drop-shadow(0 4px 12px rgba(0,0,0,0.15));}
.p-badge{position:absolute;top:12px;left:12px;z-index:2;background:var(--coral);color:#fff;font-size:11px;font-weight:700;padding:4px 10px;border-radius:var(--r-full);}
.p-stock{position:absolute;top:12px;right:12px;z-index:2;background:rgba(0,201,167,0.15);color:var(--teal-dark);font-size:11px;font-weight:700;padding:4px 10px;border-radius:var(--r-full);}
.product-body{padding:16px 18px;}
.p-id{font-size:10px;color:var(--text-soft);letter-spacing:0.5px;margin-bottom:4px;}
.p-name{font-size:16px;font-weight:700;color:var(--text-dark);line-height:1.3;margin-bottom:6px;}
.p-short{font-size:12px;color:var(--text-soft);line-height:1.4;margin-bottom:12px;}
.p-price-row{display:flex;align-items:center;gap:8px;margin-bottom:14px;}
.p-sell{font-size:20px;font-weight:800;color:var(--coral);font-family:'Fredoka',sans-serif;}
.p-mrp{font-size:13px;color:var(--text-soft);text-decoration:line-through;}
.p-disc{font-size:11px;font-weight:700;color:var(--teal-dark);background:var(--teal-light);padding:3px 8px;border-radius:var(--r-full);}
.p-btn{width:100%;background:linear-gradient(135deg,var(--coral),var(--orange));color:#fff;border:none;border-radius:var(--r-full);padding:10px;font-size:13px;font-weight:700;cursor:pointer;transition:all .2s;font-family:'Nunito',sans-serif;}
.p-btn:hover{opacity:0.9;transform:translateY(-1px);}

/* ── WHY US ── */
.why-section{background:linear-gradient(135deg,#FFF8F8,#F0FFF8);}
.why-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px;margin-top:48px;}
.why-card{background:var(--white);border-radius:var(--r-xl);padding:28px 24px;text-align:center;box-shadow:var(--shadow-sm);transition:all .25s;}
.why-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-md);}
.why-icon{width:72px;height:72px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:2rem;margin:0 auto 16px;}
.why-title{font-size:18px;font-weight:700;color:var(--text-dark);margin-bottom:8px;}
.why-text{font-size:14px;color:var(--text-soft);line-height:1.6;}

/* ── CTA BANNER ── */
.cta-banner{
  background:linear-gradient(135deg,var(--navy),var(--navy3));
  border-radius:var(--r-xl);padding:60px 48px;
  display:flex;align-items:center;justify-content:space-between;
  gap:40px;flex-wrap:wrap;margin:40px 0;
  position:relative;overflow:hidden;
}
.cta-banner::before{content:'';position:absolute;right:-80px;top:-80px;width:300px;height:300px;border-radius:50%;background:rgba(255,107,107,0.1);}
.cta-banner::after{content:'';position:absolute;left:40%;bottom:-60px;width:200px;height:200px;border-radius:50%;background:rgba(0,201,167,0.08);}
.cta-text h3{font-size:2rem;font-weight:700;color:#fff;margin-bottom:8px;}
.cta-text p{color:rgba(255,255,255,0.7);font-size:15px;}
.cta-btns{display:flex;gap:12px;flex-wrap:wrap;position:relative;z-index:1;}

/* ── FILTER TABS ── */
.filter-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-top:24px;}
.ftab{background:var(--white);border:2px solid var(--border);border-radius:var(--r-full);padding:8px 18px;font-size:13px;font-weight:700;color:var(--text-mid);cursor:pointer;transition:all .2s;font-family:'Nunito',sans-serif;}
.ftab.active,.ftab:hover{background:var(--coral);border-color:var(--coral);color:#fff;}

/* ── PRODUCT DETAIL ── */
.product-detail{max-width:1100px;margin:0 auto;padding:40px 24px;}
.detail-back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:var(--text-mid);cursor:pointer;margin-bottom:28px;transition:color .2s;}
.detail-back:hover{color:var(--coral);}
.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;}
.detail-visual{border-radius:var(--r-xl);overflow:hidden;background:linear-gradient(135deg,#F8F0FF,#FFF0F8);}
.detail-canvas-wrap{height:320px;position:relative;}
.detail-canvas-wrap canvas{position:absolute;inset:0;}
.detail-emoji-display{position:relative;z-index:1;display:flex;align-items:center;justify-content:center;height:100%;font-size:6rem;}
.detail-thumb-strip{display:flex;gap:8px;padding:12px;}
.detail-thumb{width:64px;height:64px;border-radius:12px;background:rgba(0,0,0,0.05);display:flex;align-items:center;justify-content:center;font-size:1.8rem;cursor:pointer;border:2px solid transparent;transition:all .2s;}
.detail-thumb.active{border-color:var(--coral);}
.detail-info{}
.detail-cat{font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--purple);margin-bottom:8px;}
.detail-name{font-size:2rem;font-weight:700;color:var(--text-dark);line-height:1.2;margin-bottom:8px;}
.detail-brand{font-size:14px;color:var(--text-soft);margin-bottom:20px;}
.price-box{background:linear-gradient(135deg,#FFF8F8,#FFF0E8);border-radius:var(--r-lg);padding:16px 20px;margin-bottom:20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
.price-sell{font-family:'Fredoka',sans-serif;font-size:2.2rem;font-weight:700;color:var(--coral);}
.price-mrp{font-size:16px;color:var(--text-soft);text-decoration:line-through;}
.price-disc-chip{background:var(--teal);color:#fff;font-size:13px;font-weight:700;padding:6px 14px;border-radius:var(--r-full);}
.detail-tabs{display:flex;gap:0;border-bottom:2px solid var(--border);margin-bottom:20px;}
.dtab{background:none;border:none;border-bottom:3px solid transparent;margin-bottom:-2px;padding:12px 16px;font-size:14px;font-weight:700;color:var(--text-soft);cursor:pointer;font-family:'Nunito',sans-serif;transition:all .2s;}
.dtab.active{color:var(--coral);border-bottom-color:var(--coral);}
.dtab-content{display:none;}
.dtab-content.active{display:block;}
.spec-table{width:100%;}
.spec-row{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border);font-size:14px;}
.spec-row:last-child{border-bottom:none;}
.spec-key{color:var(--text-soft);font-weight:600;}
.spec-val{color:var(--text-dark);font-weight:700;text-align:right;}
.order-btn{width:100%;background:linear-gradient(135deg,var(--teal),var(--teal-dark));color:#fff;border:none;border-radius:var(--r-full);padding:16px;font-size:16px;font-weight:800;cursor:pointer;transition:all .25s;font-family:'Nunito',sans-serif;display:flex;align-items:center;justify-content:center;gap:8px;margin-top:20px;}
.order-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,201,167,0.4);}
.review-card{background:var(--cream);border-radius:var(--r-lg);padding:14px 16px;margin-bottom:12px;}
.rv-header{display:flex;align-items:center;gap:10px;margin-bottom:6px;}
.rv-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--coral),var(--purple));display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:14px;}
.rv-name{font-size:14px;font-weight:700;color:var(--text-dark);}
.rv-date{font-size:11px;color:var(--text-soft);}
.rv-stars{color:var(--orange);font-size:13px;margin-left:auto;}
.rv-text{font-size:13px;color:var(--text-soft);line-height:1.5;}

/* ── USAGE GUIDE ── */
.guide-inner{max-width:1100px;margin:0 auto;padding:40px 24px;}
.guide-product-select{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0 40px;}
.gp-btn{background:var(--white);border:2px solid var(--border);border-radius:var(--r-full);padding:8px 20px;font-size:13px;font-weight:700;cursor:pointer;transition:all .2s;font-family:'Nunito',sans-serif;display:flex;align-items:center;gap:6px;}
.gp-btn.active,.gp-btn:hover{background:var(--purple);border-color:var(--purple);color:#fff;}
.guide-steps{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;}
.guide-step{background:var(--white);border-radius:var(--r-xl);padding:24px;box-shadow:var(--shadow-sm);position:relative;overflow:hidden;}
.guide-step::before{content:attr(data-step);position:absolute;top:-10px;right:16px;font-family:'Fredoka',sans-serif;font-size:6rem;font-weight:700;color:var(--coral);opacity:0.07;line-height:1;}
.step-num{width:36px;height:36px;background:linear-gradient(135deg,var(--coral),var(--purple));border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:14px;margin-bottom:14px;}
.step-text{font-size:14px;font-weight:600;color:var(--text-dark);line-height:1.5;margin-bottom:10px;}
.safety-note{background:var(--orange-light);border-left:3px solid var(--orange);padding:8px 12px;border-radius:0 8px 8px 0;font-size:12px;color:var(--orange-dark);font-weight:600;margin-top:8px;}

/* ── ABOUT PAGE ── */
.about-page{max-width:1100px;margin:0 auto;padding:40px 24px;}
.about-hero-strip{background:linear-gradient(135deg,var(--navy),var(--navy3));border-radius:var(--r-xl);padding:60px 48px;margin-bottom:48px;color:#fff;position:relative;overflow:hidden;}
.about-hero-strip::after{content:'🎓';position:absolute;right:48px;top:50%;transform:translateY(-50%);font-size:8rem;opacity:0.15;}
.about-hero-title{font-size:2.4rem;font-weight:700;margin-bottom:12px;}
.about-hero-sub{font-size:16px;opacity:0.8;max-width:500px;line-height:1.6;}
.contact-form{background:var(--white);border-radius:var(--r-xl);padding:40px;box-shadow:var(--shadow-md);}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;}
.form-group{display:flex;flex-direction:column;gap:6px;}
.form-group label{font-size:13px;font-weight:700;color:var(--text-dark);}
.form-group input,.form-group textarea,.form-group select{border:2px solid var(--border);border-radius:var(--r-md);padding:12px 14px;font-size:14px;font-family:'Nunito',sans-serif;color:var(--text-dark);background:var(--cream);transition:border-color .2s;outline:none;}
.form-group input:focus,.form-group textarea:focus{border-color:var(--coral);}
.form-group textarea{resize:vertical;min-height:100px;}
.form-submit{background:linear-gradient(135deg,var(--coral),var(--orange));color:#fff;border:none;border-radius:var(--r-full);padding:14px 32px;font-size:15px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;transition:all .25s;}
.form-submit:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(255,107,107,0.4);}

/* ── FAQ ── */
.faq-inner{max-width:800px;margin:0 auto;padding:40px 24px;}
.faq-item{background:var(--white);border-radius:var(--r-lg);margin-bottom:12px;overflow:hidden;box-shadow:var(--shadow-sm);}
.faq-q{width:100%;display:flex;align-items:center;justify-content:space-between;padding:18px 20px;font-size:15px;font-weight:700;color:var(--text-dark);cursor:pointer;background:none;border:none;text-align:left;font-family:'Nunito',sans-serif;gap:12px;}
.faq-q:hover{color:var(--coral);}
.faq-arrow{font-size:18px;transition:transform .25s;flex-shrink:0;color:var(--coral);}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease,padding .3s;font-size:14px;color:var(--text-soft);line-height:1.6;}
.faq-a.open{max-height:200px;padding:0 20px 18px;}
.faq-arrow.open{transform:rotate(180deg);}

/* ── REVIEWS PAGE ── */
.reviews-inner{max-width:1100px;margin:0 auto;padding:40px 24px;}
.rating-summary{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin-bottom:48px;}
.rating-card{background:var(--white);border-radius:var(--r-xl);padding:20px;text-align:center;box-shadow:var(--shadow-sm);}
.rating-emoji{font-size:2.5rem;margin-bottom:8px;}
.rating-name{font-size:13px;font-weight:700;color:var(--text-dark);margin-bottom:4px;line-height:1.3;}
.rating-stars{color:var(--orange);font-size:15px;margin-bottom:4px;}
.review-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;}
.review-big-card{background:var(--white);border-radius:var(--r-xl);padding:24px;box-shadow:var(--shadow-sm);}
.rb-header{display:flex;align-items:center;gap:12px;margin-bottom:14px;}
.rb-avatar{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--coral),var(--purple));display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:16px;flex-shrink:0;}
.rb-name{font-size:15px;font-weight:700;color:var(--text-dark);}
.rb-sub{font-size:12px;color:var(--text-soft);}
.rb-stars{font-size:14px;color:var(--orange);margin-bottom:10px;}
.rb-text{font-size:14px;color:var(--text-soft);line-height:1.6;}

/* ── CONTACT ── */
.contact-inner{max-width:900px;margin:0 auto;padding:40px 24px;}
.contact-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:40px;align-items:start;}
.contact-info-card{background:linear-gradient(135deg,var(--navy),var(--navy3));border-radius:var(--r-xl);padding:36px;color:#fff;}
.ci-title{font-size:1.4rem;font-weight:700;margin-bottom:24px;}
.ci-item{display:flex;align-items:center;gap:12px;margin-bottom:18px;font-size:14px;}
.ci-icon{width:40px;height:40px;background:rgba(255,255,255,0.1);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0;}
.wa-btn{width:100%;background:#25D366;color:#fff;border:none;border-radius:var(--r-full);padding:14px;font-size:15px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;margin-top:24px;display:flex;align-items:center;justify-content:center;gap:8px;transition:all .25s;}
.wa-btn:hover{background:#1DB954;transform:translateY(-2px);}
.social-row{display:flex;gap:10px;margin-top:20px;}
.social-icon{width:40px;height:40px;background:rgba(255,255,255,0.1);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;cursor:pointer;transition:background .2s;}
.social-icon:hover{background:rgba(255,255,255,0.2);}

/* ── FOOTER ── */
footer{background:var(--navy);color:#fff;padding:60px 24px 32px;}
.footer-inner{max-width:1200px;margin:0 auto;}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:48px;}
.footer-brand{font-size:24px;font-weight:700;color:var(--coral);margin-bottom:12px;}
.footer-brand span{color:var(--teal);}
.footer-desc{font-size:14px;color:rgba(255,255,255,0.6);line-height:1.6;margin-bottom:16px;}
.footer-col-title{font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:16px;}
.footer-link{display:block;font-size:14px;color:rgba(255,255,255,0.7);cursor:pointer;margin-bottom:8px;transition:color .2s;}
.footer-link:hover{color:var(--coral);}
.footer-social{display:flex;gap:10px;margin-top:8px;}
.footer-social-icon{width:36px;height:36px;background:rgba(255,255,255,0.1);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1rem;cursor:pointer;transition:background .2s;}
.footer-social-icon:hover{background:var(--coral);}
.footer-divider{border:none;border-top:1px solid rgba(255,255,255,0.1);margin-bottom:24px;}
.footer-bottom{display:flex;align-items:center;justify-content:space-between;font-size:13px;color:rgba(255,255,255,0.5);}

/* ── CHATBOT ── */
.chatbot-fab{position:fixed;bottom:28px;right:28px;z-index:900;}
.chat-toggle{width:60px;height:60px;background:linear-gradient(135deg,var(--coral),var(--purple));border:none;border-radius:50%;cursor:pointer;font-size:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(255,107,107,0.4);transition:all .3s;position:relative;}
.chat-toggle:hover{transform:scale(1.1);}
.chat-badge{position:absolute;top:-4px;right:-4px;width:18px;height:18px;background:var(--teal);border-radius:50%;border:2px solid var(--cream);}
.chat-window-wrap{position:absolute;bottom:72px;right:0;width:340px;background:var(--white);border-radius:var(--r-xl);box-shadow:var(--shadow-lg);overflow:hidden;display:none;flex-direction:column;border:1px solid var(--border);}
.chat-window-wrap.open{display:flex;}
.chat-head{background:linear-gradient(135deg,var(--navy),var(--navy3));padding:16px 18px;display:flex;align-items:center;gap:10px;}
.chat-head-info{flex:1;}
.chat-head-name{font-size:15px;font-weight:700;color:#fff;}
.chat-head-status{font-size:12px;color:rgba(255,255,255,0.6);}
.chat-head-close{background:none;border:none;color:rgba(255,255,255,0.6);cursor:pointer;font-size:18px;line-height:1;}
.chat-msgs{height:280px;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;}
.cmsg{max-width:82%;font-size:13px;line-height:1.5;padding:10px 13px;border-radius:16px;}
.cmsg.bot{background:var(--cream);color:var(--text-dark);align-self:flex-start;border-bottom-left-radius:4px;}
.cmsg.user{background:linear-gradient(135deg,var(--coral),var(--orange));color:#fff;align-self:flex-end;border-bottom-right-radius:4px;}
.cmsg.typing{color:var(--text-soft);font-style:italic;}
.chat-result{background:var(--white);border:1px solid var(--border);border-radius:12px;padding:10px 12px;margin-top:4px;cursor:pointer;transition:border-color .2s;}
.chat-result:hover{border-color:var(--coral);}
.chat-result-name{font-size:13px;font-weight:700;color:var(--text-dark);}
.chat-result-price{font-size:13px;color:var(--coral);font-weight:700;}
.chat-input-bar{display:flex;gap:8px;padding:12px;border-top:1px solid var(--border);}
.chat-input-bar input{flex:1;border:2px solid var(--border);border-radius:var(--r-full);padding:8px 14px;font-size:13px;font-family:'Nunito',sans-serif;outline:none;transition:border-color .2s;}
.chat-input-bar input:focus{border-color:var(--coral);}
.chat-send{background:linear-gradient(135deg,var(--coral),var(--orange));color:#fff;border:none;border-radius:50%;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;}

/* ── ANIMATIONS ── */
.fade-in{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s ease;}
.fade-in.visible{opacity:1;transform:translateY(0);}
@keyframes spin{to{transform:rotate(360deg);}}
@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-12px);}}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .hero-content{grid-template-columns:1fr;}
  .hero-visual{display:none;}
  .about-inner{grid-template-columns:1fr;}
  .detail-grid{grid-template-columns:1fr;}
  .footer-grid{grid-template-columns:1fr 1fr;}
  .form-row{grid-template-columns:1fr;}
  .contact-grid{grid-template-columns:1fr;}
}
</style>
</head>
<body>

<!-- NAV -->
<nav id="mainNav">
  <div class="nav-inner">
    <div class="nav-logo" onclick="showPage('home')">EduKit<span>Connect</span></div>
    <div class="nav-links">
      <button class="nav-link active" onclick="showPage('home')">Home</button>
      <button class="nav-link" onclick="showPage('shop')">Shop</button>
      <button class="nav-link" onclick="showPage('guide')">Usage Guide</button>
      <button class="nav-link" onclick="showPage('about')">About</button>
      <button class="nav-link" onclick="showPage('faq')">FAQ</button>
      <button class="nav-link" onclick="showPage('reviews')">Reviews</button>
      <button class="nav-link" onclick="showPage('contact')">Contact</button>
    </div>
    <button class="nav-cta" onclick="showPage('shop')">Browse Products &rarr;</button>
  </div>
</nav>

<!-- HOME PAGE -->
<div class="page active" id="page-home">

  <!-- HERO -->
  <section class="hero">
    <canvas class="hero-canvas" id="heroCanvas"></canvas>
    <div class="hero-content">
      <div>
        <div class="hero-eyebrow"><span></span> Hyderabad's #1 Educational Toy Marketplace</div>
        <h1>Learn it.<br><em>Build it.</em><br><strong>See it.</strong></h1>
        <p class="hero-sub">Educational kits for curious minds. Connecting Hyderabad parents and schools with the finest hands-on learning products &mdash; from builders to scientists to puzzlers.</p>
        <div class="hero-btns">
          <button class="btn-primary" onclick="showPage('shop')">&#x1F6D2; Explore Products</button>
          <button class="btn-outline" onclick="showPage('guide')">&#x1F4D6; Usage Guide</button>
        </div>
        <div class="hero-stats">
          <div class="hstat"><div class="hstat-num">10+</div><div class="hstat-label">Products</div></div>
          <div class="hstat"><div class="hstat-num">4.7&#9733;</div><div class="hstat-label">Avg Rating</div></div>
          <div class="hstat"><div class="hstat-num">&#8377;15</div><div class="hstat-label">Starts at</div></div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-orb">
          <canvas id="heroOrbCanvas" width="380" height="380"></canvas>
        </div>
      </div>
    </div>
  </section>

  <!-- ABOUT STRIP -->
  <div class="about-strip">
    <div class="about-inner">
      <div>
        <div class="about-badge">&#x1F393;</div>
        <div class="about-title">About Navnirmiti Eduquality</div>
        <p class="about-body">We are a Hyderabad-based educational toy company with one mission: make learning tangible. Every kit we produce is designed to get children's hands moving and minds thinking &mdash; no screens required. From classic puzzles to STEM builders, our products are trusted by hundreds of Hyderabad families and schools.</p>
      </div>
      <div class="about-right">
        <div class="about-card"><div class="about-card-icon">&#x1F512;</div><div class="about-card-title">Safe &amp; Tested</div><div class="about-card-text">All products are child-safe, non-toxic and age-tested before reaching you.</div></div>
        <div class="about-card"><div class="about-card-icon">&#x1F9E0;</div><div class="about-card-title">Curriculum-Aligned</div><div class="about-card-text">Designed to complement school learning for ages 6&ndash;12.</div></div>
        <div class="about-card"><div class="about-card-icon">&#x1F4B8;</div><div class="about-card-title">Affordable</div><div class="about-card-text">Starting at just &#8377;15 &mdash; quality education shouldn't cost a fortune.</div></div>
        <div class="about-card"><div class="about-card-icon">&#x1F91D;</div><div class="about-card-title">Made in India</div><div class="about-card-text">Proudly produced in Hyderabad, supporting local craftsmanship.</div></div>
      </div>
    </div>
  </div>

  <!-- FEATURED PRODUCTS -->
  <section class="section" style="background:var(--cream);">
    <div class="section-inner">
      <div class="section-label">Most Loved</div>
      <h2 class="section-title">Featured <em>Products</em></h2>
      <p class="section-sub">Hand-picked bestsellers that parents and teachers love most.</p>
      <div class="products-grid" id="featuredGrid"></div>
      <div style="text-align:center;margin-top:40px;">
        <button class="btn-primary" onclick="showPage('shop')">View All Products &rarr;</button>
      </div>
    </div>
  </section>

  <!-- WHY US -->
  <section class="section why-section">
    <div class="section-inner">
      <div class="section-label">Why EduKit Connect</div>
      <h2 class="section-title">Learning that <em>feels like play</em></h2>
      <div class="why-grid">
        <div class="why-card fade-in"><div class="why-icon" style="background:#FFF0F8;"><span>&#x1F6E1;&#xFE0F;</span></div><div class="why-title">100% Safe</div><div class="why-text">Every product is non-toxic, age-appropriate and rigorously tested. Your child's safety is our first priority.</div></div>
        <div class="why-card fade-in"><div class="why-icon" style="background:#F0FFF8;"><span>&#x1F9E9;</span></div><div class="why-title">Hands-On Learning</div><div class="why-text">Screen-free play builds real cognitive skills &mdash; spatial reasoning, creativity and problem-solving.</div></div>
        <div class="why-card fade-in"><div class="why-icon" style="background:#FFF8F0;"><span>&#x1F4A1;</span></div><div class="why-title">Curriculum-Linked</div><div class="why-text">Products align with science, maths and geography concepts taught in school. Learning extends beyond the classroom.</div></div>
        <div class="why-card fade-in"><div class="why-icon" style="background:#F8F0FF;"><span>&#x1F4B0;</span></div><div class="why-title">Genuinely Affordable</div><div class="why-text">From &#8377;15 to &#8377;999 &mdash; we believe every child in Hyderabad deserves access to quality learning tools.</div></div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" style="background:var(--white);">
    <div class="section-inner">
      <div class="cta-banner">
        <div class="cta-text">
          <h3>Ready to spark curiosity?</h3>
          <p>Browse our full catalog or get the complete usage guide for free.</p>
        </div>
        <div class="cta-btns">
          <button class="btn-primary" onclick="showPage('shop')">&#x1F6D2; Browse Products</button>
          <button class="btn-outline" onclick="showPage('guide')">&#x1F4D6; Get the Usage Guide</button>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <div class="footer-inner">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">EduKit<span>Connect</span></div>
          <p class="footer-desc">Connecting Hyderabad families with hands-on educational toys that make learning joyful and screen-free.</p>
          <div class="footer-social">
            <div class="footer-social-icon">&#x1F4D8;</div>
            <div class="footer-social-icon">&#x1F4F8;</div>
            <div class="footer-social-icon">&#x1F426;</div>
            <div class="footer-social-icon">&#x25B6;&#xFE0F;</div>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Quick Links</div>
          <span class="footer-link" onclick="showPage('home')">Home</span>
          <span class="footer-link" onclick="showPage('shop')">Shop</span>
          <span class="footer-link" onclick="showPage('guide')">Usage Guide</span>
          <span class="footer-link" onclick="showPage('about')">About</span>
        </div>
        <div>
          <div class="footer-col-title">Support</div>
          <span class="footer-link" onclick="showPage('faq')">FAQ</span>
          <span class="footer-link" onclick="showPage('reviews')">Reviews</span>
          <span class="footer-link" onclick="showPage('contact')">Contact</span>
        </div>
        <div>
          <div class="footer-col-title">Contact</div>
          <p class="footer-link">&#x1F4CD; Hyderabad, Telangana</p>
          <p class="footer-link">&#x1F4DE; +91 98765 43210</p>
          <p class="footer-link">&#x2709;&#xFE0F; hello@edukitconnect.in</p>
        </div>
      </div>
      <hr class="footer-divider">
      <div class="footer-bottom">
        <span>&copy; 2026 Navnirmiti Eduquality. All rights reserved.</span>
        <span>Made with &#x2764;&#xFE0F; in Hyderabad</span>
      </div>
    </div>
  </footer>
</div>

<!-- SHOP PAGE -->
<div class="page" id="page-shop">
  <section class="section" style="padding-top:40px;">
    <div class="section-inner">
      <div class="section-label">All Products</div>
      <h2 class="section-title">Our <em>Products</em></h2>
      <p class="section-sub">Discover 10 carefully crafted educational kits &mdash; puzzles, builders, science tools and more.</p>
      <div class="filter-tabs" id="shopFilters">
        <button class="ftab active" onclick="filterShop('All',this)">All Products</button>
        <button class="ftab" onclick="filterShop('Educational Puzzle',this)">&#x1F537; Puzzles</button>
        <button class="ftab" onclick="filterShop('STEM Building Kit',this)">&#x1F3D7;&#xFE0F; STEM Kits</button>
        <button class="ftab" onclick="filterShop('Science',this)">&#x1F52C; Science</button>
        <button class="ftab" onclick="filterShop('Math Learning Tool',this)">&#x1F9EE; Math</button>
        <button class="ftab" onclick="filterShop('STEM Learning Game',this)">&#x1F47E; Games</button>
      </div>
      <div class="products-grid" id="shopGrid"></div>
    </div>
  </section>
  <footer>
    <div class="footer-inner">
      <div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span><span class="footer-link" onclick="showPage('home')">&larr; Back to Home</span></div>
    </div>
  </footer>
</div>

<!-- PRODUCT DETAIL PAGE -->
<div class="page" id="page-product">
  <div class="product-detail" id="productDetailContent"></div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span><span class="footer-link" onclick="showPage('shop')">&larr; Back to Shop</span></div></div></footer>
</div>

<!-- USAGE GUIDE PAGE -->
<div class="page" id="page-guide">
  <div class="guide-inner">
    <div class="section-label">Step-by-Step</div>
    <h2 class="section-title">Usage <em>Guide</em></h2>
    <p class="section-sub">Learn how to get the most from every EduKit product &mdash; with safety tips and fun challenges included.</p>
    <div class="guide-product-select" id="guideProductBtns"></div>
    <div class="guide-steps" id="guideSteps"></div>
  </div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span><span class="footer-link" onclick="showPage('home')">&larr; Home</span></div></div></footer>
</div>

<!-- ABOUT PAGE -->
<div class="page" id="page-about">
  <div class="about-page">
    <div class="about-hero-strip">
      <div class="section-label" style="color:var(--teal);">Our Story</div>
      <div class="about-hero-title">Navnirmiti Eduquality</div>
      <p class="about-hero-sub">We started with a simple belief: children learn best when they can touch, build and explore. From a small workshop in Hyderabad, we now reach hundreds of families and schools with hands-on educational kits.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-bottom:48px;">
      <div style="background:var(--white);border-radius:var(--r-xl);padding:28px;box-shadow:var(--shadow-sm);">
        <div style="font-size:2rem;margin-bottom:12px;">&#x1F3AF;</div>
        <h3 style="font-size:1.2rem;margin-bottom:8px;">Our Mission</h3>
        <p style="font-size:14px;color:var(--text-soft);line-height:1.6;">To make quality educational tools accessible to every child in Hyderabad, bridging the gap between rote learning and true understanding through play-based education.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--r-xl);padding:28px;box-shadow:var(--shadow-sm);">
        <div style="font-size:2rem;margin-bottom:12px;">&#x1F441;&#xFE0F;</div>
        <h3 style="font-size:1.2rem;margin-bottom:8px;">Our Vision</h3>
        <p style="font-size:14px;color:var(--text-soft);line-height:1.6;">A Hyderabad where every child has access to screen-free learning tools that develop creativity, critical thinking and a love for discovery.</p>
      </div>
    </div>
    <div class="contact-form">
      <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:6px;">Producer / School Connect</h3>
      <p style="font-size:14px;color:var(--text-soft);margin-bottom:24px;">Are you a school or bulk buyer? Reach out for special pricing and partnerships.</p>
      <div class="form-row">
        <div class="form-group"><label>Name</label><input type="text" placeholder="Your full name"></div>
        <div class="form-group"><label>Organisation</label><input type="text" placeholder="School or company name"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label>Email</label><input type="email" placeholder="your@email.com"></div>
        <div class="form-group"><label>Phone</label><input type="tel" placeholder="+91 98765 43210"></div>
      </div>
      <div class="form-group" style="margin-bottom:20px;"><label>Message</label><textarea placeholder="Tell us about your bulk requirement or partnership idea..."></textarea></div>
      <button class="form-submit" onclick="alert('Thank you! We will get back to you within 24 hours.')">Send Message &rarr;</button>
    </div>
  </div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span></div></div></footer>
</div>

<!-- FAQ PAGE -->
<div class="page" id="page-faq">
  <div class="faq-inner">
    <div class="section-label">Got Questions?</div>
    <h2 class="section-title">Frequently Asked <em>Questions</em></h2>
    <p class="section-sub" style="margin-bottom:36px;">Everything you need to know about our products, orders and safety.</p>
    <div id="faqList"></div>
    <div style="background:linear-gradient(135deg,var(--coral-light),var(--purple-light));border-radius:var(--r-xl);padding:32px;text-align:center;margin-top:40px;">
      <h3 style="font-size:1.3rem;margin-bottom:8px;">Still have questions?</h3>
      <p style="font-size:14px;color:var(--text-soft);margin-bottom:20px;">Our team is happy to help you find the right kit for your child.</p>
      <button class="btn-primary" onclick="showPage('contact')">Contact Us &rarr;</button>
    </div>
  </div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span></div></div></footer>
</div>

<!-- REVIEWS PAGE -->
<div class="page" id="page-reviews">
  <div class="reviews-inner">
    <div class="section-label">What Parents Say</div>
    <h2 class="section-title">Customer <em>Reviews</em></h2>
    <p class="section-sub" style="margin-bottom:40px;">Real reviews from Hyderabad families who use our products every day.</p>
    <div class="rating-summary" id="ratingSummary"></div>
    <div class="review-grid" id="reviewGrid"></div>
    <div style="text-align:center;margin-top:40px;">
      <button class="btn-primary" onclick="alert('Review form coming soon! For now, message us on WhatsApp.')">&#x2B50; Leave a Review</button>
    </div>
  </div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span></div></div></footer>
</div>

<!-- CONTACT PAGE -->
<div class="page" id="page-contact">
  <div class="contact-inner">
    <div class="section-label">Get in Touch</div>
    <h2 class="section-title" style="margin-bottom:36px;">Contact <em>Us</em></h2>
    <div class="contact-grid">
      <div class="contact-info-card">
        <div class="ci-title">Navnirmiti Eduquality</div>
        <div class="ci-item"><div class="ci-icon">&#x1F4CD;</div><span>Hyderabad, Telangana, India</span></div>
        <div class="ci-item"><div class="ci-icon">&#x1F4DE;</div><span>+91 98765 43210</span></div>
        <div class="ci-item"><div class="ci-icon">&#x2709;&#xFE0F;</div><span>hello@edukitconnect.in</span></div>
        <div class="ci-item"><div class="ci-icon">&#x1F550;</div><span>Mon&ndash;Sat, 9am&ndash;6pm IST</span></div>
        <button class="wa-btn" onclick="alert('Opening WhatsApp...')">&#x1F4AC; Order via WhatsApp</button>
        <div class="social-row">
          <div class="social-icon">&#x1F4D8;</div><div class="social-icon">&#x1F4F8;</div><div class="social-icon">&#x1F426;</div><div class="social-icon">&#x25B6;&#xFE0F;</div>
        </div>
      </div>
      <div class="contact-form">
        <h3 style="font-size:1.2rem;font-weight:700;margin-bottom:20px;">Send us a message</h3>
        <div class="form-group" style="margin-bottom:16px;"><label>Name</label><input type="text" placeholder="Your name"></div>
        <div class="form-group" style="margin-bottom:16px;"><label>Email</label><input type="email" placeholder="your@email.com"></div>
        <div class="form-group" style="margin-bottom:20px;"><label>Message</label><textarea placeholder="How can we help you?"></textarea></div>
        <button class="form-submit" onclick="alert('Message sent! We will reply within 24 hours.')">Send Message &rarr;</button>
      </div>
    </div>
  </div>
  <footer><div class="footer-inner"><div class="footer-bottom"><span>&copy; 2026 Navnirmiti Eduquality</span></div></div></footer>
</div>

<!-- CHATBOT -->
<div class="chatbot-fab">
  <div class="chat-window-wrap" id="chatWindow">
    <div class="chat-head">
      <div style="width:36px;height:36px;background:linear-gradient(135deg,var(--coral),var(--purple));border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.2rem;">&#x1F916;</div>
      <div class="chat-head-info"><div class="chat-head-name">EduKit Assistant</div><div class="chat-head-status">&#x25CF; Online &mdash; describe a toy!</div></div>
      <button class="chat-head-close" onclick="toggleChat()">&times;</button>
    </div>
    <div class="chat-msgs" id="chatMsgs">
      <div class="cmsg bot">Hi! &#x1F44B; Describe the toy or kit you're looking for and I'll find it &mdash; or log your request for our producers!</div>
    </div>
    <div class="chat-input-bar">
      <input type="text" id="chatInput" placeholder="e.g. building kit for 8 year old..." onkeydown="if(event.key==='Enter')sendChat()">
      <button class="chat-send" onclick="sendChat()">&#x27A4;</button>
    </div>
  </div>
  <button class="chat-toggle" onclick="toggleChat()">&#x1F916;<div class="chat-badge"></div></button>
</div>

<script>
/* DATA */
const PRODUCTS = [
  {sno:1,id:'EQ-TAN-001',name:'Tangram – 216 Puzzles',cat:'Educational Puzzle',brand:'Navnirmiti Eduquality',short:'Build shapes, animals and objects with 216 puzzle combinations',full:'A classic tangram set with 7 geometric pieces that combine into 216 different puzzle shapes. Helps improve spatial reasoning, logic and creativity in children through screen-free play.',size:'Standard – 7 piece set',mrp:250,sell:199,disc:'20%',age:'6–12',stock:'In Stock',emoji:'🔷',hue:'#A855F7',bg:'#F3E8FF'},
  {sno:2,id:'EQ-STK-002',name:'Sticks & Connectors Building Kit',cat:'STEM Building Kit',brand:'Navnirmiti Eduquality',short:'Construct towers, bridges and structures with this STEM kit',full:'A creative construction kit with colorful sticks and connectors that can be assembled into towers, bridges, animals and structures. Encourages fine motor skills, teamwork and engineering thinking.',size:'Family Pack – 200+ pieces',mrp:450,sell:399,disc:'12%',age:'6–12',stock:'In Stock',emoji:'🏗️',hue:'#00C9A7',bg:'#E0FBF5'},
  {sno:3,id:'EQ-SOL-003',name:'Solar Eclipse Viewing Glasses',cat:'Science Safety Equipment',brand:'Navnirmiti Eduquality',short:'Safely view solar eclipses with certified solar filters',full:'Solar filter glasses that protect the eyes while allowing safe direct viewing of the sun during an eclipse. Recommended for short, restricted viewing periods only.',size:'One Size – Universal Fit',mrp:15,sell:15,disc:'0%',age:'6–12',stock:'In Stock',emoji:'🕶️',hue:'#FF9500',bg:'#FFF3E0'},
  {sno:4,id:'EQ-MAG-004',name:'Magnetic Building Blocks Set',cat:'STEM Building Kit',brand:'Navnirmiti Eduquality',short:'Build 3D shapes and structures using magnetic tiles',full:'A set of colorful magnetic tiles that snap together to form 3D geometric shapes, houses, vehicles and more. Builds spatial awareness, creativity and an early understanding of geometry.',size:'Standard – 60 piece set',mrp:899,sell:749,disc:'17%',age:'6–12',stock:'In Stock',emoji:'🧲',hue:'#FF6B6B',bg:'#FFE8E8'},
  {sno:5,id:'EQ-SCI-005',name:'Junior Science Experiment Kit',cat:'Science Kit',brand:'Navnirmiti Eduquality',short:'Conduct 20+ safe and simple science experiments at home',full:'A beginner-friendly science kit with safe materials and an instruction booklet to perform over 20 experiments covering chemistry, physics and basic biology concepts.',size:'Compact Box – 25+ components',mrp:699,sell:599,disc:'14%',age:'8–12',stock:'In Stock',emoji:'🔬',hue:'#378ADD',bg:'#E6F1FB'},
  {sno:6,id:'EQ-ABA-006',name:'Wooden Abacus Counting Frame',cat:'Math Learning Tool',brand:'Navnirmiti Eduquality',short:'Learn counting, addition and subtraction with colourful beads',full:'A traditional wooden abacus with 100 colorful beads, helping young children grasp number sense, counting and basic arithmetic through hands-on movement.',size:'Standard – 10 rows / 100 beads',mrp:350,sell:299,disc:'15%',age:'6–9',stock:'In Stock',emoji:'🧮',hue:'#639922',bg:'#EAF3DE'},
  {sno:7,id:'EQ-PUZ-007',name:'World Map Floor Puzzle',cat:'Educational Puzzle',brand:'Navnirmiti Eduquality',short:'A giant floor puzzle to learn countries and continents',full:'A large 48-piece floor puzzle of the world map, helping children learn geography, country names and continents while playing on the floor with friends.',size:'Large – 48 pieces (90cm \xD7 60cm)',mrp:499,sell:399,disc:'20%',age:'6–12',stock:'In Stock',emoji:'🗺️',hue:'#A855F7',bg:'#F3E8FF'},
  {sno:8,id:'EQ-COD-008',name:'Beginner Coding Board Game',cat:'STEM Learning Game',brand:'Navnirmiti Eduquality',short:'Learn the basics of coding logic without using a screen',full:'A screen-free board game that introduces children to coding concepts like sequencing, loops and conditionals through fun challenge cards and a game board.',size:'Standard Box – 2 to 4 players',mrp:799,sell:699,disc:'13%',age:'8–12',stock:'In Stock',emoji:'👾',hue:'#00C9A7',bg:'#E0FBF5'},
  {sno:9,id:'EQ-MIC-009',name:'Beginner Microscope Kit',cat:'Science Kit',brand:'Navnirmiti Eduquality',short:'Explore the micro world with a real working microscope',full:'An entry-level microscope kit with prepared slides, tools and a guidebook, letting children explore cells, insects, fabrics and everyday objects up close.',size:'Compact – with 5 slides & tools',mrp:1199,sell:999,disc:'17%',age:'9–12',stock:'In Stock',emoji:'🔭',hue:'#378ADD',bg:'#E6F1FB'},
  {sno:10,id:'EQ-CLK-010',name:'Learning Clock & Calendar Set',cat:'Educational Tool',brand:'Navnirmiti Eduquality',short:'Teach kids to read time and understand calendars',full:'A colorful wooden clock with movable hands paired with a calendar chart, helping children practice telling time, days, months and seasons.',size:'Standard Set – Clock + Calendar Chart',mrp:399,sell:329,disc:'18%',age:'6–9',stock:'In Stock',emoji:'🕐',hue:'#FF9500',bg:'#FFF3E0'}
];

const USAGE = {
  'EQ-TAN-001':[{n:1,t:'Open the pack and remove all 7 tangram pieces from the tray',s:null},{n:2,t:'Look at the puzzle card for the shape you want to build',s:null},{n:3,t:'Arrange all 7 pieces without overlapping to match the outline',s:null},{n:4,t:'Try building your own shapes once you finish the puzzle cards',s:null}],
  'EQ-STK-002':[{n:1,t:'Sort the sticks and connectors by colour and size',s:null},{n:2,t:'Pick a structure idea such as a tower, bridge or animal',s:null},{n:3,t:'Connect sticks using the connectors to form the base',s:null},{n:4,t:'Build upward or outward layer by layer',s:'Keep small connector pieces away from children under 3 years'}],
  'EQ-SOL-003':[{n:1,t:'Check that the solar film is not torn or damaged before use',s:'Do not use if the film is torn or damaged'},{n:2,t:'Wear the glasses fully covering both eyes before looking at the sun',s:'Never remove the glasses while looking directly at the sun'},{n:3,t:'View the sun for short durations only and take breaks',s:'Continuous viewing should be restricted'},{n:4,t:'Remove the glasses only after looking away from the sun',s:'Adult supervision recommended for children'}],
  'EQ-MAG-004':[{n:1,t:'Sort the magnetic tiles by shape – triangles, squares and others',s:null},{n:2,t:'Start with a flat base shape by connecting tiles edge to edge',s:null},{n:3,t:'Add vertical tiles to build walls and form a 3D structure',s:null},{n:4,t:'Combine multiple shapes to build houses, animals or vehicles',s:'Keep away from children under 3 due to small magnetic parts'}],
  'EQ-SCI-005':[{n:1,t:'Read the instruction booklet before starting any experiment',s:'Adult supervision required for all experiments'},{n:2,t:'Gather the required components listed for the chosen experiment',s:null},{n:3,t:'Follow the steps in order and observe the results carefully',s:'Do not taste or inhale any experiment materials'},{n:4,t:'Clean and store all components back in the kit after use',s:'Wash hands after completing each experiment'}],
  'EQ-ABA-006':[{n:1,t:'Place the abacus on a flat surface with rows facing you',s:null},{n:2,t:'Slide one bead at a time to count from 1 to 10',s:null},{n:3,t:'Use two rows together to practise simple addition',s:null},{n:4,t:'Slide beads back to practise subtraction problems',s:null}],
  'EQ-PUZ-007':[{n:1,t:'Lay out a flat clear space such as the floor or a large table',s:null},{n:2,t:'Sort edge pieces first and form the outer border',s:null},{n:3,t:'Fill in continents one at a time using colours as a guide',s:null},{n:4,t:'Once complete, try naming countries and continents aloud',s:null}],
  'EQ-COD-008':[{n:1,t:'Set up the game board and shuffle the challenge cards',s:null},{n:2,t:'Draw a card and plan a sequence of moves to reach the goal',s:null},{n:3,t:'Place direction tiles in order to represent your code sequence',s:null},{n:4,t:'Run the sequence step by step and adjust if it does not work',s:null}],
  'EQ-MIC-009':[{n:1,t:'Place the microscope on a flat, stable surface',s:'Handle glass slides carefully to avoid breakage'},{n:2,t:'Place a prepared slide on the stage and secure with the clips',s:null},{n:3,t:'Adjust the focus knob slowly until the image becomes clear',s:null},{n:4,t:'Try preparing your own slide with a leaf or fabric sample',s:'Adult supervision recommended when preparing slides'}],
  'EQ-CLK-010':[{n:1,t:"Set the clock hands to a time of day, for example 7 o'clock",s:null},{n:2,t:'Practise reading the hour and minute hands aloud',s:null},{n:3,t:"Use the calendar chart to find today's date, day and month",s:null},{n:4,t:'Mark important dates like birthdays on the calendar',s:null}]
};

const FAQS = [
  {q:'Is it safe for kids?',a:'Yes, all products are designed and tested to be safe for children aged 6 to 12 when used as instructed.',cat:'General'},
  {q:'What age group is this for?',a:'Our products are best suited for children between 6 and 12 years old.',cat:'General'},
  {q:'How do I place an order?',a:'You can order directly through the website or contact us via WhatsApp using the Order Now button on any product page.',cat:'General'},
  {q:'What if the product is damaged?',a:'Contact us within 48 hours of delivery with photos of the damaged product and we will arrange a replacement.',cat:'General'},
  {q:'Do you offer bulk or school discounts?',a:'Yes, schools and bulk buyers can contact us through the Producer Connect page for special pricing.',cat:'General'},
  {q:'How many puzzles can be made with the tangram set?',a:'The set includes 216 different puzzle combinations ranging from easy to difficult.',cat:'Tangram'},
  {q:'Are the sticks and connectors reusable?',a:'Yes, the sticks and connectors can be disassembled and reused to build different structures repeatedly.',cat:'Sticks & Connectors'},
  {q:'Can I reuse the solar glasses for multiple eclipses?',a:'Yes, as long as the solar film is not torn, scratched or damaged, it can be reused.',cat:'Solar Glasses'},
  {q:'How long can I view the sun continuously?',a:'Continuous viewing should be restricted. Take short breaks every few seconds for safety.',cat:'Solar Glasses'},
  {q:'How long does delivery take?',a:'Orders are typically processed and delivered within 3 to 5 business days within Hyderabad.',cat:'Shipping'},
  {q:'Are small magnetic parts safe for younger siblings?',a:'The magnetic tiles contain small magnets and are recommended only for children aged 6 and above. Keep away from toddlers.',cat:'Magnetic Blocks'},
  {q:'Are the chemicals in the science kit safe?',a:'Yes, all materials are non-toxic and child-safe, but adult supervision is recommended during experiments.',cat:'Science Kit'},
  {q:'Does the microscope kit include slides?',a:'Yes, it comes with 5 prepared slides along with basic tools to prepare your own slides.',cat:'Microscope'},
  {q:'Do I need a screen or app to play the coding game?',a:'No, the entire game is screen-free and played using physical cards and tiles.',cat:'Coding Game'},
  {q:'What payment methods are accepted?',a:'Currently we accept payments via UPI and cash on delivery. Card payments will be added soon.',cat:'Payments'}
];

const REVIEWS = [
  {id:'EQ-TAN-001',name:'Anjali Rao',rating:5,text:'My daughter loves solving the tangram puzzles. Great for keeping her away from the phone.',date:'May 12, 2026'},
  {id:'EQ-TAN-001',name:'Suresh Kumar',rating:4,text:'Good quality pieces and the puzzle book has a lot of variety. Slightly small box.',date:'May 20, 2026'},
  {id:'EQ-STK-002',name:'Priya Menon',rating:5,text:'Wonderful kit. My son built a small bridge and a tower the first day itself.',date:'Jun 1, 2026'},
  {id:'EQ-STK-002',name:'Ramesh Iyer',rating:4,text:'Lots of pieces and very durable. Took some time to sort initially.',date:'Jun 3, 2026'},
  {id:'EQ-SOL-003',name:'Lakshmi Narayan',rating:5,text:'Affordable and worked perfectly during the eclipse. Easy for kids to wear.',date:'Apr 15, 2026'},
  {id:'EQ-MAG-004',name:'Divya Sharma',rating:5,text:'Kids spent hours building houses and shapes. Very strong magnets, great quality.',date:'May 28, 2026'},
  {id:'EQ-SCI-005',name:'Kiran Reddy',rating:4,text:'Good variety of experiments. Instructions could be a bit more detailed for younger kids.',date:'May 30, 2026'},
  {id:'EQ-ABA-006',name:'Rohit Verma',rating:5,text:'Simple but effective for teaching counting to my 6 year old.',date:'Apr 22, 2026'},
  {id:'EQ-PUZ-007',name:'Meera Pillai',rating:5,text:'Big and colorful, perfect for learning geography while having fun on the floor.',date:'Jun 5, 2026'},
  {id:'EQ-COD-008',name:'Arjun Nair',rating:4,text:'Great concept to introduce coding without a screen. My son enjoys the challenge cards.',date:'Jun 8, 2026'},
  {id:'EQ-MIC-009',name:'Sneha Joshi',rating:5,text:'My daughter is fascinated looking at fabric and leaves under the microscope.',date:'May 18, 2026'},
  {id:'EQ-CLK-010',name:'Vikram Das',rating:4,text:'Helped my son finally understand reading analog clocks. Calendar chart is a nice addition.',date:'Apr 30, 2026'}
];

/* CANVAS ANIMATIONS */
let animFrameId = null;
const particlePool = [];
let heroTime = 0;

function initHeroCanvas(){
  const c = document.getElementById('heroCanvas');
  if(!c) return;
  c.width = c.offsetWidth; c.height = c.offsetHeight;
  const ctx = c.getContext('2d');
  const particles = [];
  for(let i=0;i<60;i++) particles.push({x:Math.random()*c.width,y:Math.random()*c.height,r:Math.random()*3+1,vx:(Math.random()-0.5)*0.4,vy:(Math.random()-0.5)*0.4,o:Math.random()*0.4+0.1,emoji:['✦','◆','●','▲','■'][Math.floor(Math.random()*5)],fs:Math.random()*14+8});
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    particles.forEach(p=>{
      ctx.globalAlpha=p.o;
      ctx.fillStyle='rgba(255,255,255,0.6)';
      ctx.font=p.fs+'px sans-serif';
      ctx.fillText(p.emoji,p.x,p.y);
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<0)p.x=c.width; if(p.x>c.width)p.x=0;
      if(p.y<0)p.y=c.height; if(p.y>c.height)p.y=0;
    });
    ctx.globalAlpha=1;
    requestAnimationFrame(draw);
  }
  draw();
}

function drawOrbAnimation(){
  const c = document.getElementById('heroOrbCanvas');
  if(!c) return;
  const ctx = c.getContext('2d');
  const cx=190, cy=190, t=heroTime;
  ctx.clearRect(0,0,380,380);
  const grad = ctx.createRadialGradient(cx,cy,60,cx,cy,180);
  grad.addColorStop(0,'rgba(255,107,107,0.15)');
  grad.addColorStop(0.5,'rgba(168,85,247,0.1)');
  grad.addColorStop(1,'rgba(0,201,167,0.05)');
  ctx.fillStyle=grad; ctx.beginPath(); ctx.arc(cx,cy,175,0,Math.PI*2); ctx.fill();
  const orbitEmojis=['🔷','🏗️','🔬','🧲','🧮','👾','🗺️','🔭'];
  orbitEmojis.forEach((em,i)=>{
    const angle=t*0.008+i*Math.PI*2/orbitEmojis.length;
    const r=130+(i%2)*20;
    const ex=cx+Math.cos(angle)*r, ey=cy+Math.sin(angle)*r;
    ctx.font='24px sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.globalAlpha=0.85+Math.sin(t*0.05+i)*0.15;
    ctx.fillText(em,ex,ey);
  });
  ctx.globalAlpha=1;
  ctx.font='60px sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
  ctx.fillText('⭐',cx,cy+Math.sin(t*0.03)*6);
  for(let i=0;i<6;i++){
    const a=t*0.02+i*Math.PI/3, r=70+Math.sin(t*0.04+i)*10;
    const sx=cx+Math.cos(a)*r, sy=cy+Math.sin(a)*r;
    ctx.globalAlpha=0.4+Math.sin(t*0.05+i)*0.3;
    ctx.fillStyle='#FFD60A'; ctx.font='12px sans-serif'; ctx.fillText('✦',sx,sy);
  }
  ctx.globalAlpha=1;
  heroTime++;
  requestAnimationFrame(drawOrbAnimation);
}

/* PRODUCT CARD CANVAS */
let cardAnims = {};
function startCardAnim(id, canvasId, p){
  if(cardAnims[id]) return;
  const c = document.getElementById(canvasId);
  if(!c) return;
  const ctx = c.getContext('2d');
  c.width=c.offsetWidth||260; c.height=200;
  let t=0;
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    const cx=c.width/2, cy=100;
    drawProductMini(ctx,p,cx,cy,t);
    t++;
    cardAnims[id] = requestAnimationFrame(draw);
  }
  draw();
}

function drawProductMini(ctx,p,cx,cy,t){
  const angle=t*0.015;
  if(p.id.includes('TAN')){
    const pieces=[{dx:-35,dy:-15,sides:3,rot:angle},{dx:5,dy:-25,sides:4,rot:angle+0.5},{dx:40,dy:-10,sides:3,rot:angle+1},{dx:-15,dy:20,sides:3,rot:angle+1.5}];
    pieces.forEach((pc,i)=>drawPoly(ctx,cx+pc.dx,cy+pc.dy,pc.sides,22,pc.rot,['#A855F7','#FF6B6B','#00C9A7','#FF9500'][i]));
  } else if(p.id.includes('STK')||p.id.includes('MAG')){
    for(let i=0;i<6;i++){const ax=Math.cos(angle+i*Math.PI/3)*50,ay=Math.sin(angle+i*Math.PI/3)*38;drawCube(ctx,cx+ax,cy+ay,16,p.hue);}
    drawCube(ctx,cx,cy,22,p.hue);
  } else if(p.id.includes('SOL')){
    ctx.strokeStyle=p.hue; ctx.lineWidth=3;
    for(let i=0;i<8;i++){const ra=angle+i*Math.PI/4;ctx.beginPath();ctx.moveTo(cx+Math.cos(ra)*38,cy+Math.sin(ra)*28);ctx.lineTo(cx+Math.cos(ra)*60,cy+Math.sin(ra)*44);ctx.stroke();}
    ctx.beginPath();ctx.ellipse(cx,cy,34,22,0,0,Math.PI*2);ctx.fillStyle=p.hue+'33';ctx.fill();ctx.stroke();
    ctx.beginPath();ctx.arc(cx,cy,16,0,Math.PI*2);ctx.fillStyle=p.hue;ctx.fill();
  } else if(p.id.includes('ABA')){
    for(let row=0;row<4;row++){for(let col=0;col<4;col++){const bx=cx+(col-1.5)*20+Math.sin(t*0.04+row)*3,by=cy+(row-1.5)*20;ctx.beginPath();ctx.arc(bx,by,8,0,Math.PI*2);ctx.fillStyle=col%2?'#FF6B6B':'#00C9A7';ctx.fill();}}
  } else if(p.id.includes('PUZ')){
    const cc=['#9FE1CB','#AFA9EC','#FAC775','#F0997B','#85B7EB','#C0DD97'];
    for(let i=0;i<6;i++){const a=angle*0.5+i*Math.PI/3;ctx.beginPath();ctx.ellipse(cx+Math.cos(a)*44,cy+Math.sin(a)*30,18,12,a,0,Math.PI*2);ctx.fillStyle=cc[i];ctx.fill();}
  } else if(p.id.includes('COD')){
    ['{ }','if','for','=>'].forEach((lbl,i)=>{const a=angle+i*Math.PI/2;const ex=cx+Math.cos(a)*48,ey=cy+Math.sin(a)*34;ctx.fillStyle=p.hue+'33';ctx.beginPath();ctx.roundRect(ex-18,ey-10,36,20,4);ctx.fill();ctx.fillStyle=p.hue;ctx.font='bold 11px monospace';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(lbl,ex,ey);});
  } else if(p.id.includes('CLK')){
    ctx.strokeStyle=p.hue;ctx.lineWidth=3;ctx.beginPath();ctx.arc(cx-20,cy,38,0,Math.PI*2);ctx.stroke();
    const ha=angle,ma=angle*12;
    ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(cx-20,cy);ctx.lineTo(cx-20+Math.cos(ha-Math.PI/2)*24,cy+Math.sin(ha-Math.PI/2)*24);ctx.stroke();
    ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(cx-20,cy);ctx.lineTo(cx-20+Math.cos(ma-Math.PI/2)*32,cy+Math.sin(ma-Math.PI/2)*32);ctx.stroke();
    ctx.fillStyle=p.hue+'33';ctx.beginPath();ctx.roundRect(cx+12,cy-26,42,52,6);ctx.fill();ctx.strokeStyle=p.hue;ctx.lineWidth=1.5;ctx.strokeRect(cx+12,cy-26,42,52);
    ctx.fillStyle=p.hue;ctx.font='bold 14px Fredoka,sans-serif';ctx.textAlign='center';ctx.fillText('13',cx+33,cy+6);ctx.font='10px sans-serif';ctx.fillText('JUN',cx+33,cy-10);
  } else {
    for(let i=0;i<5;i++){const a=angle+i*Math.PI*2/5;drawPoly(ctx,cx+Math.cos(a)*44,cy+Math.sin(a)*30,6,16,a,p.hue);}
    ctx.beginPath();ctx.arc(cx,cy,18,0,Math.PI*2);ctx.fillStyle=p.hue+'88';ctx.fill();
    ctx.font='20px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(p.emoji,cx,cy);
  }
}

function drawPoly(ctx,x,y,sides,r,rot,color){
  ctx.save();ctx.translate(x,y);ctx.rotate(rot);
  ctx.beginPath();
  for(let i=0;i<sides;i++){ctx.lineTo(Math.cos(i*Math.PI*2/sides-Math.PI/2)*r,Math.sin(i*Math.PI*2/sides-Math.PI/2)*r);}
  ctx.closePath();ctx.fillStyle=color+'cc';ctx.fill();ctx.restore();
}

function drawCube(ctx,x,y,sz,color){
  const h=sz*0.6;
  ctx.save();ctx.translate(x,y);
  ctx.fillStyle=color+'cc';ctx.beginPath();ctx.moveTo(0,-sz);ctx.lineTo(h,-sz+h*0.5);ctx.lineTo(h,h*0.5);ctx.lineTo(0,sz*0.5);ctx.closePath();ctx.fill();
  ctx.fillStyle=color+'99';ctx.beginPath();ctx.moveTo(0,-sz);ctx.lineTo(-h,-sz+h*0.5);ctx.lineTo(-h,h*0.5);ctx.lineTo(0,sz*0.5);ctx.closePath();ctx.fill();
  ctx.fillStyle=color+'ee';ctx.beginPath();ctx.moveTo(-h,-sz+h*0.5);ctx.lineTo(0,-sz);ctx.lineTo(h,-sz+h*0.5);ctx.lineTo(0,-sz+h);ctx.closePath();ctx.fill();
  ctx.restore();
}

/* RENDER HELPERS */
function makeProductCard(p){
  const canId='canvas-'+p.id+'-'+Math.random().toString(36).slice(2);
  return `<div class="product-card" onclick="openProduct('${p.id}')">
    <div class="product-thumb" style="background:${p.bg};">
      <canvas id="${canId}" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
      ${p.disc!=='0%'?`<span class="p-badge">${p.disc} OFF</span>`:''}
      <span class="p-stock">✓ In Stock</span>
    </div>
    <div class="product-body">
      <div class="p-id">${p.id} · S.No ${p.sno}</div>
      <div class="p-name">${p.name}</div>
      <div class="p-short">${p.short}</div>
      <div class="p-price-row">
        <span class="p-sell">₹${p.sell}</span>
        ${p.mrp!==p.sell?`<span class="p-mrp">₹${p.mrp}</span><span class="p-disc">${p.disc} off</span>`:''}
      </div>
      <button class="p-btn">View Details →</button>
    </div>
  </div>`;
}

function initCardCanvases(){
  document.querySelectorAll('.product-thumb canvas').forEach(c=>{
    const id=c.id;
    const pid=id.match(/canvas-(EQ-\w+-\d+)/)?.[1];
    const p=PRODUCTS.find(x=>x.id===pid);
    if(p&&!cardAnims[id]){
      setTimeout(()=>startCardAnim(id,id,p),100);
    }
  });
}

function stopAllCardAnims(){
  Object.entries(cardAnims).forEach(([id,f])=>{cancelAnimationFrame(f);});
  cardAnims={};
}

/* PAGE ROUTING */
function showPage(name){
  stopAllCardAnims();
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));
  document.getElementById('page-'+name).classList.add('active');
  const link=document.querySelector(`.nav-link[onclick*="'${name}'"]`);
  if(link) link.classList.add('active');
  window.scrollTo(0,0);
  setTimeout(()=>{
    if(name==='home'){renderFeatured();}
    else if(name==='shop'){renderShop();}
    else if(name==='guide'){renderGuide();}
    else if(name==='faq'){renderFAQ();}
    else if(name==='reviews'){renderReviews();}
    observeFadeIns();
    initCardCanvases();
  },50);
}

function renderFeatured(){
  const el=document.getElementById('featuredGrid');
  if(!el) return;
  el.innerHTML=PRODUCTS.slice(0,3).map(p=>makeProductCard(p)).join('');
}

function renderShop(filter='All'){
  const el=document.getElementById('shopGrid');
  if(!el) return;
  const filtered=filter==='All'?PRODUCTS:PRODUCTS.filter(p=>p.cat.includes(filter));
  el.innerHTML=filtered.map(p=>makeProductCard(p)).join('');
}

function filterShop(filter, btn){
  document.querySelectorAll('.ftab').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  stopAllCardAnims();
  renderShop(filter);
  setTimeout(initCardCanvases,100);
}

function openProduct(id){
  const p=PRODUCTS.find(x=>x.id===id);
  if(!p) return;
  const revs=REVIEWS.filter(r=>r.id===id);
  const steps=USAGE[id]||[];
  const canId='detail-canvas-'+id;
  document.getElementById('productDetailContent').innerHTML=`
    <div class="detail-back" onclick="showPage('shop')">← Back to Shop</div>
    <div class="detail-grid">
      <div class="detail-visual">
        <div class="detail-canvas-wrap" style="background:${p.bg};">
          <canvas id="${canId}" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
        </div>
        <div class="detail-thumb-strip">
          <div class="detail-thumb active">${p.emoji}</div>
          <div class="detail-thumb">🔍</div>
          <div class="detail-thumb">📦</div>
        </div>
      </div>
      <div class="detail-info">
        <div class="detail-cat">${p.cat}</div>
        <div class="detail-name">${p.name}</div>
        <div class="detail-brand">by ${p.brand} · Ages ${p.age}</div>
        <div class="price-box">
          <span class="price-sell">₹${p.sell}</span>
          ${p.mrp!==p.sell?`<span class="price-mrp">₹${p.mrp}</span><span class="price-disc-chip">${p.disc} off</span>`:''}
        </div>
        <div class="detail-tabs">
          <button class="dtab active" onclick="switchTab(this,'tab-desc')">Description</button>
          <button class="dtab" onclick="switchTab(this,'tab-specs')">Specifications</button>
          <button class="dtab" onclick="switchTab(this,'tab-usage')">Usage Guide</button>
          <button class="dtab" onclick="switchTab(this,'tab-reviews')">Reviews (${revs.length})</button>
        </div>
        <div id="tab-desc" class="dtab-content active"><p style="font-size:14px;color:var(--text-soft);line-height:1.7;">${p.full}</p></div>
        <div id="tab-specs" class="dtab-content">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-key">Product ID</span><span class="spec-val">${p.id}</span></div>
            <div class="spec-row"><span class="spec-key">S.No</span><span class="spec-val">${p.sno}</span></div>
            <div class="spec-row"><span class="spec-key">Size</span><span class="spec-val">${p.size}</span></div>
            <div class="spec-row"><span class="spec-key">Brand</span><span class="spec-val">${p.brand}</span></div>
            <div class="spec-row"><span class="spec-key">Category</span><span class="spec-val">${p.cat}</span></div>
            <div class="spec-row"><span class="spec-key">Age Group</span><span class="spec-val">Ages ${p.age}</span></div>
            <div class="spec-row"><span class="spec-key">MRP</span><span class="spec-val">₹${p.mrp}</span></div>
            <div class="spec-row"><span class="spec-key">Sell Price</span><span class="spec-val">₹${p.sell}</span></div>
            <div class="spec-row"><span class="spec-key">Discount</span><span class="spec-val">${p.disc}</span></div>
            <div class="spec-row"><span class="spec-key">Stock Status</span><span class="spec-val" style="color:var(--teal-dark);">✓ ${p.stock}</span></div>
          </div>
        </div>
        <div id="tab-usage" class="dtab-content">
          ${steps.map(s=>`<div style="display:flex;gap:12px;margin-bottom:14px;"><div style="width:28px;height:28px;min-width:28px;background:linear-gradient(135deg,var(--coral),var(--purple));border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px;font-weight:800;">${s.n}</div><div><p style="font-size:14px;font-weight:600;color:var(--text-dark);margin-bottom:4px;">${s.t}</p>${s.s?`<p style="font-size:12px;color:var(--orange-dark);background:var(--orange-light);padding:4px 10px;border-radius:6px;border-left:3px solid var(--orange);">⚠️ ${s.s}</p>`:''}</div></div>`).join('')}
        </div>
        <div id="tab-reviews" class="dtab-content">
          ${revs.length?revs.map(r=>`<div class="review-card"><div class="rv-header"><div class="rv-avatar">${r.name.charAt(0)}</div><div><div class="rv-name">${r.name}</div><div class="rv-date">${r.date}</div></div><div class="rv-stars">${'★'.repeat(r.rating)}${'☆'.repeat(5-r.rating)}</div></div><div class="rv-text">${r.text}</div></div>`).join(''):'<p style="font-size:14px;color:var(--text-soft);padding:12px 0;">No reviews yet — be the first!</p>'}
        </div>
        <button class="order-btn" onclick="alert('Opening WhatsApp to order ${p.name.replace(/'/g,"\\'")}...')">💬 Order Now via WhatsApp</button>
      </div>
    </div>
  `;
  showPage('product');
  setTimeout(()=>{
    const c=document.getElementById(canId);
    if(c){c.width=c.offsetWidth||500;c.height=320;let t2=0;function anim2(){const ctx=c.getContext('2d');ctx.clearRect(0,0,c.width,c.height);drawProductMini(ctx,p,c.width/2,c.height/2,t2);t2++;requestAnimationFrame(anim2);}anim2();}
  },100);
}

function switchTab(btn, tabId){
  const parent=btn.closest('.detail-info');
  parent.querySelectorAll('.dtab').forEach(t=>t.classList.remove('active'));
  parent.querySelectorAll('.dtab-content').forEach(t=>t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById(tabId).classList.add('active');
}

/* USAGE GUIDE */
function renderGuide(selectedId=null){
  const btnEl=document.getElementById('guideProductBtns');
  const stepsEl=document.getElementById('guideSteps');
  if(!btnEl||!stepsEl) return;
  const active=selectedId||PRODUCTS[0].id;
  btnEl.innerHTML=PRODUCTS.map(p=>`<button class="gp-btn ${p.id===active?'active':''}" onclick="renderGuide('${p.id}')">${p.emoji} ${p.name.split('–')[0].split('(')[0].trim()}</button>`).join('');
  const steps=USAGE[active]||[];
  stepsEl.innerHTML=steps.map(s=>`<div class="guide-step fade-in" data-step="${s.n}"><div class="step-num">${s.n}</div><div class="step-text">${s.t}</div>${s.s?`<div class="safety-note">⚠️ ${s.s}</div>`:''}</div>`).join('');
  observeFadeIns();
}

/* FAQ */
function renderFAQ(){
  const el=document.getElementById('faqList');
  if(!el) return;
  el.innerHTML=FAQS.map((f,i)=>`<div class="faq-item"><button class="faq-q" onclick="toggleFAQ(${i})"><span>${f.q}</span><span class="faq-arrow" id="farrow-${i}">▼</span></button><div class="faq-a" id="fans-${i}">${f.a}</div></div>`).join('');
}
function toggleFAQ(i){
  const a=document.getElementById('fans-'+i);
  const arr=document.getElementById('farrow-'+i);
  a.classList.toggle('open');
  arr.classList.toggle('open');
}

/* REVIEWS */
function renderReviews(){
  const sumEl=document.getElementById('ratingSummary');
  const gridEl=document.getElementById('reviewGrid');
  if(!sumEl||!gridEl) return;
  const byProduct={};
  REVIEWS.forEach(r=>{if(!byProduct[r.id])byProduct[r.id]={reviews:[],total:0};byProduct[r.id].reviews.push(r);byProduct[r.id].total+=r.rating;});
  sumEl.innerHTML=Object.entries(byProduct).map(([id,d])=>{
    const p=PRODUCTS.find(x=>x.id===id);
    const avg=(d.total/d.reviews.length).toFixed(1);
    return `<div class="rating-card"><div class="rating-emoji">${p.emoji}</div><div class="rating-name">${p.name}</div><div class="rating-stars">${'★'.repeat(Math.round(avg))}${'☆'.repeat(5-Math.round(avg))}</div><div style="font-size:13px;font-weight:700;color:var(--text-dark);">${avg} / 5 <span style="color:var(--text-soft);font-weight:400;">(${d.reviews.length})</span></div></div>`;
  }).join('');
  gridEl.innerHTML=REVIEWS.map(r=>{
    const p=PRODUCTS.find(x=>x.id===r.id);
    return `<div class="review-big-card"><div class="rb-header"><div class="rb-avatar">${r.name.charAt(0)}</div><div><div class="rb-name">${r.name}</div><div class="rb-sub">on ${p?p.name:'Product'} · ${r.date}</div></div></div><div class="rb-stars">${'★'.repeat(r.rating)}${'☆'.repeat(5-r.rating)}</div><div class="rb-text">${r.text}</div></div>`;
  }).join('');
}

/* CHATBOT */
function toggleChat(){document.getElementById('chatWindow').classList.toggle('open');}
function addMsg(text,type){const el=document.getElementById('chatMsgs');const d=document.createElement('div');d.className='cmsg '+type;d.innerHTML=text;el.appendChild(d);el.scrollTop=el.scrollHeight;}
function removeTyping(){document.querySelectorAll('.cmsg.typing').forEach(e=>e.remove());}

async function sendChat(){
  const inp=document.getElementById('chatInput');
  const msg=inp.value.trim();
  if(!msg)return;
  inp.value='';
  addMsg(msg,'user');
  addMsg('Searching...','bot typing');
  const found=searchProducts(msg);
  await new Promise(r=>setTimeout(r,600));
  removeTyping();
  if(found.length){
    addMsg(`Found ${found.length} match${found.length>1?'es':''}!`,'bot');
    found.forEach(p=>{
      const d=document.createElement('div');
      d.className='cmsg bot';
      d.style.maxWidth='88%';
      d.innerHTML=`<div class="chat-result" onclick="openProduct('${p.id}');toggleChat()"><div style="display:flex;gap:8px;align-items:center;"><span style="font-size:1.4rem;">${p.emoji}</span><div><div class="chat-result-name">${p.name}</div><div class="chat-result-price">₹${p.sell} <span style="color:var(--text-soft);font-size:11px;text-decoration:line-through;">₹${p.mrp}</span></div></div></div></div>`;
      document.getElementById('chatMsgs').appendChild(d);
      document.getElementById('chatMsgs').scrollTop=99999;
    });
  } else {
    addMsg("I couldn't find that yet — logging your request for our producers! 📋",'bot');
    try{
      const res=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({model:'claude-sonnet-4-6',max_tokens:1000,system:"You are EduKit Connect's helpful assistant for Hyderabad parents. The user wants a toy not in the catalog. Empathize warmly in 2 sentences, ask one clarifying question about age/subject/budget. Be friendly, under 60 words.",messages:[{role:'user',content:`Looking for: "${msg}"`}]})});
      const data=await res.json();
      const text=data.content?.[0]?.text||"Thanks! We've noted your request and will inform our producers. Could you share the age group and budget?";
      addMsg(text,'bot');
    } catch{addMsg("Thanks! We've noted your request and will notify our producers. Can you share the age group and your budget?","bot");}
    addMsg('📋 Your demand has been logged and sent to Navnirmiti Eduquality.','bot');
  }
}

function searchProducts(q){
  q=q.toLowerCase();
  const kw=q.split(/\s+/);
  return PRODUCTS.map(p=>{
    let sc=0;
    const txt=(p.name+' '+p.cat+' '+p.short+' '+p.full+' '+p.age).toLowerCase();
    kw.forEach(k=>{if(txt.includes(k))sc+=k.length>3?2:1;});
    if(q.includes('build')&&p.cat.includes('STEM'))sc+=3;
    if(q.includes('puzzle')&&p.cat.includes('Puzzle'))sc+=3;
    if(q.includes('science'))sc+=p.cat.includes('Science')?3:0;
    if(q.includes('math'))sc+=p.cat.includes('Math')?3:0;
    const am=q.match(/(\d+)\s*year/);
    if(am){const ag=parseInt(am[1]);const[lo,hi]=p.age.split('–').map(Number);if(ag>=lo&&ag<=hi)sc+=3;}
    return {p,sc};
  }).filter(x=>x.sc>=2).sort((a,b)=>b.sc-a.sc).slice(0,3).map(x=>x.p);
}

/* SCROLL & INTERSECTION */
function observeFadeIns(){
  const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:0.1});
  document.querySelectorAll('.fade-in').forEach(el=>obs.observe(el));
}

window.addEventListener('scroll',()=>{
  document.getElementById('mainNav').classList.toggle('scrolled',window.scrollY>10);
});

/* INIT */
window.addEventListener('load',()=>{
  initHeroCanvas();
  drawOrbAnimation();
  renderFeatured();
  renderGuide();
  renderFAQ();
  renderReviews();
  setTimeout(()=>{initCardCanvases();observeFadeIns();},200);
});
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=True)
