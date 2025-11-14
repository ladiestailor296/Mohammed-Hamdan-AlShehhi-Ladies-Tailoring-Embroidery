/* ===========================================
   PROFESSIONAL MULTI-AD NETWORK INTEGRATION
   Google | Meta | TikTok | Snapchat | YouTube
   Arabic Audience Optimized (UAE/KSA/GCC)
   Auto + Manual Tracking + Smart Optimization
=============================================== */

// ================= 1. GOOGLE ADSENSE (AUTO ADS) =================
(function loadGoogleAds() {
    const script = document.createElement('script');
    script.async = true;
    script.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXX";
    script.crossOrigin = "anonymous";
    document.head.appendChild(script);

    script.onload = () => {
        (adsbygoogle = window.adsbygoogle || []).push({
            google_ad_client: "ca-pub-XXXX",
            enable_page_level_ads: true,
            language: "ar",
            geo_targeting: ["AE","SA","KW","QA","OM","BH"]
        });
    };
})();

// ================= 2. META (FACEBOOK + INSTAGRAM PIXEL) =================
!function(f,b,e,v,n,t,s){
    if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)
}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_META_PIXEL_ID');
fbq('track', 'PageView', {language: 'ar', region: 'UAE'});

// ================= 3. TIKTOK PIXEL =================
(function(w,d,t){
    w.TiktokAnalyticsObject=t;
    var ttq=w[t]=w[t]||[];
    ttq.methods=["page","track","identify"];
    ttq.setAndDefer=function(obj,method){
        obj[method]=function(){obj.push([method].concat(Array.prototype.slice.call(arguments,0)));};
    };
    for(var i=0;i<ttq.methods.length;i++){ttq.setAndDefer(ttq,ttq.methods[i]);}
    ttq.load=function(pix){
        var u="https://analytics.tiktok.com/i18n/pixel/events.js";
        ttq._i=ttq._i||{};ttq._i[pix]=[];
        var e=d.createElement("script");e.async=!0;e.src=u+"?sdkid="+pix+"&lib="+t;
        var s=d.getElementsByTagName("script")[0];s.parentNode.insertBefore(e,s);
    };
    ttq.load('YOUR_TIKTOK_PIXEL_ID');
    ttq.page({language: "ar", region: "GCC"});
})(window,document,'ttq');

// ================= 4. SNAPCHAT PIXEL =================
(function(w,d){
    if(w.snaptr)return; var s=w.snaptr=function(){s.handleRequest?s.handleRequest.apply(s,arguments):s.queue.push(arguments)};
    s.queue=[]; var e=d.createElement('script'); e.async=!0; e.src='https://sc-static.net/scevent.min.js';
    var n=d.getElementsByTagName('script')[0]; n.parentNode.insertBefore(e,n);
})(window,document);
snaptr('init','YOUR_SNAP_PIXEL_ID');
snaptr('track','PAGE_VIEW',{lang:"ar", country:"AE"});

// ================= 5. YOUTUBE VIDEO TRACKING =================
function trackYouTubeView(video_id){
    fbq('track','ViewContent',{video:video_id});
    ttq.track('ViewContent',{video:video_id});
    snaptr('track','VIEW_CONTENT',{video:video_id});
}

// ================= 6. SMART AD SLOT OPTIMIZATION =================
function optimizeAds(){
    console.log("Smart Ads Optimization Running…");
    const refreshInterval = 45000; // 45 seconds

    // Refresh ads automatically
    setInterval(()=>{
        const adSlots = document.querySelectorAll('.ad-box');
        adSlots.forEach(slot=>{
            slot.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-format="auto"></ins>';
        });
        (adsbygoogle = window.adsbygoogle || []).push({});
    }, refreshInterval);

    // Detect user interest
    const interest = localStorage.getItem("interest_category");
    console.log("User interest:", interest);
}
document.addEventListener("DOMContentLoaded", optimizeAds);

// ================= 7. TRACKING FUNCTIONS (AUTO + MANUAL) =================
function trackEvent(eventName, details){
    fbq('track', eventName, details);
    ttq.track(eventName, details);
    snaptr('track', eventName.toUpperCase(), details);
}

function trackProductView(product_id, name, price){
    trackEvent("ViewContent",{product_id, name, price});
}

function trackAddToCart(product_id, price){
    trackEvent("AddToCart",{product_id, price});
}

function trackPurchase(order_id, amount){
    trackEvent("Purchase",{order_id, value:amount, currency:"AED"});
}

// ================= 8. ARABIC AUDIENCE BOOST =================
function boostArabicAds(){
    const lang = navigator.language || navigator.userLanguage;
    if(lang.includes("ar")){
        document.body.classList.add("arabic-user");
        console.log("Arabic Audience Boost Active");
    }
}
boostArabicAds();
