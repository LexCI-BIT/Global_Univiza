import os
import re

def fix_index_html():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        return
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Replace the entire svc-container block
    new_grid = """    <div class="svc-container">
      <div class="svc-grid" id="svcGrid">
        <a href="service-details.html?id=test-preparation" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-test-prep.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg></div>
              <h3>Test Preparation</h3>
            </div>
            <p>IELTS, TOEFL, GRE, GMAT — expert coaching to hit your target scores.</p>
          </div>
        </a>
        <a href="service-details.html?id=admission-counselling" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-admission.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg></div>
              <h3>Admission Counselling</h3>
            </div>
            <p>Personalised one-on-one sessions to map out your academic future.</p>
          </div>
        </a>
        <a href="service-details.html?id=profile-evaluation" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-profile.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 14h6"></path><path d="M9 18h6"></path><path d="M9 10h6"></path></svg></div>
              <h3>Profile Evaluation</h3>
            </div>
            <p>Smart university shortlisting based on your profile and aspirations.</p>
          </div>
        </a>
        <a href="service-details.html?id=education-loans" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-loans.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
              <h3>Education Loans</h3>
            </div>
            <p>Best-rate loans via 6 leading Indian bank partners.</p>
          </div>
        </a>
        <a href="service-details.html?id=visa-guidance" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-visa.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
              <h3>Visa Guidance & Mocks</h3>
            </div>
            <p>Documentation, mock interviews and step-by-step visa support.</p>
          </div>
        </a>
        <a href="service-details.html?id=travel-assistance" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-travel.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a2 2 0 0 0-2 2v5L3 13.5v2L10 14v5l-2 1.5v1.5l4-1 4 1v-1.5L14 19v-5l7 1.5v-2L14 10V5a2 2 0 0 0-2-2z" transform="rotate(45 12 12)"/></svg></div>
              <h3>Travel Assistance</h3>
            </div>
            <p>Flight booking, pre-departure briefing and air ticket arrangements.</p>
          </div>
        </a>
        <a href="service-details.html?id=accommodation" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-accommodation.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg></div>
              <h3>Accommodation</h3>
            </div>
            <p>Safe, affordable student housing near your campus abroad.</p>
          </div>
        </a>
        <a href="service-details.html?id=part-time-guidance" class="sc" style="text-decoration:none; color:inherit; background-image: url('assets/svc-part-time.png');">
          <div class="sc-inner-box">
            <div class="sc-header">
              <div class="si"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></div>
              <h3>Part-time Guidance</h3>
            </div>
            <p>Legal part-time work opportunities to support yourself abroad.</p>
          </div>
        </a>
      </div>
    </div>"""
    
    # Use regex to replace the entire <div class="svc-container">...</div>
    content = re.sub(r'<div class="svc-container">.*?</div>\s*</div>', new_grid + '\n    </div>', content, flags=re.DOTALL)
    
    # 2. Replace the linearScroller script
    new_script = """    // Auto-scroll for Premium Services (Continuous Linear)
    const svcGrid = document.querySelector('.svc-grid');
    if (svcGrid) {
      // 1. Only duplicate content ONCE for seamless infinite scrolling
      const originalCards = Array.from(svcGrid.children);
      originalCards.forEach(card => svcGrid.appendChild(card.cloneNode(true)));
      
      let isInteracting = false;
      let scrollPos = svcGrid.scrollLeft;

      // 2. Pause auto-scroll on interaction
      svcGrid.addEventListener('mouseenter', () => isInteracting = true);
      svcGrid.addEventListener('mouseleave', () => isInteracting = false);
      svcGrid.addEventListener('touchstart', () => isInteracting = true, { passive: true });
      svcGrid.addEventListener('touchend', () => {
        setTimeout(() => isInteracting = false, 2000);
      }, { passive: true });

      // 3. Calculate actual reset point
      let resetPoint = 0;
      function calculateReset() {
        const cards = Array.from(svcGrid.children);
        if (cards.length > originalCards.length) {
          resetPoint = cards[originalCards.length].offsetLeft - cards[0].offsetLeft;
        }
      }
      setTimeout(calculateReset, 100);
      window.addEventListener('resize', calculateReset);

      // 4. Continuous scroll loop
      function step() {
        if (!isInteracting && resetPoint > 0) {
          if (svcGrid.style.scrollSnapType !== 'none') {
            svcGrid.style.scrollSnapType = 'none';
          }
          scrollPos += 0.8; 
          if (scrollPos >= resetPoint) {
            scrollPos -= resetPoint;
          }
          svcGrid.scrollLeft = scrollPos;
        } else {
          scrollPos = svcGrid.scrollLeft;
          if (svcGrid.style.scrollSnapType === 'none') {
            svcGrid.style.scrollSnapType = '';
          }
        }
        requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }"""
    
    content = re.sub(r'// Auto-scroll for Premium Services.*?requestAnimationFrame\(linearScroller\);[ \t\n]*\}', new_script, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html")

def fix_service_data():
    filepath = 'service-data.js'
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove all \ufffd (represented as \xef\xbf\xbd in utf-8)
    sanitized = content.encode('utf-8', 'ignore').decode('utf-8').replace('\ufffd', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(sanitized)
    print("Fixed service-data.js")

if __name__ == "__main__":
    fix_index_html()
    fix_service_data()
