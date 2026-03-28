import os

def final_sanitize(filepath):
    if not os.path.isfile(filepath):
        print(f"Skipping {filepath}")
        return
    
    # Read binary to be safe
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # EF BF BD is the UTF-8 replacement char
    corrupted = b'\xef\xbf\xbd'
    
    if corrupted in data:
        count = data.count(corrupted)
        print(f"Removing {count} instances of corruption from {filepath}")
        sanitized = data.replace(corrupted, b'')
        with open(filepath, 'wb') as f:
            f.write(sanitized)
    else:
        print(f"No corruption found in {filepath}")

def fix_marquee_logic():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        return
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    new_lines = []
    in_script = False
    for line in lines:
        # If we find the marquee block, we'll replace it with a clean one
        if 'const svcGrid = document.querySelector(\'.svc-grid\');' in line:
            in_script = True
            new_lines.append("    const svcGrid = document.querySelector('.svc-grid');\n")
            new_lines.append("    if (svcGrid) {\n")
            new_lines.append("      // 1. Only duplicate content once for seamless looping\n")
            new_lines.append("      const originalCards = Array.from(svcGrid.children);\n")
            new_lines.append("      originalCards.forEach(card => svcGrid.appendChild(card.cloneNode(true)));\n")
            new_lines.append("      \n")
            new_lines.append("      let isInteracting = false;\n")
            new_lines.append("      let scrollPos = svcGrid.scrollLeft;\n")
            new_lines.append("\n")
            new_lines.append("      svcGrid.addEventListener('mouseenter', () => isInteracting = true);\n")
            new_lines.append("      svcGrid.addEventListener('mouseleave', () => isInteracting = false);\n")
            new_lines.append("      svcGrid.addEventListener('touchstart', () => isInteracting = true, { passive: true });\n")
            new_lines.append("      svcGrid.addEventListener('touchend', () => setTimeout(() => isInteracting = false, 2000), { passive: true });\n")
            new_lines.append("\n")
            new_lines.append("      let resetPoint = 0;\n")
            new_lines.append("      function calculateReset() {\n")
            new_lines.append("        const cards = Array.from(svcGrid.children);\n")
            new_lines.append("        if (cards.length > originalCards.length) {\n")
            new_lines.append("          resetPoint = cards[originalCards.length].offsetLeft - cards[0].offsetLeft;\n")
            new_lines.append("        }\n")
            new_lines.append("      }\n")
            new_lines.append("      setTimeout(calculateReset, 100);\n")
            new_lines.append("      window.addEventListener('resize', calculateReset);\n")
            new_lines.append("\n")
            new_lines.append("      function step() {\n")
            new_lines.append("        if (!isInteracting && resetPoint > 0) {\n")
            new_lines.append("          if (svcGrid.style.scrollSnapType !== 'none') svcGrid.style.scrollSnapType = 'none';\n")
            new_lines.append("          scrollPos += 0.8;\n")
            if "scrollPos >= resetPoint" not in line: # Logic check
                new_lines.append("          if (scrollPos >= resetPoint) scrollPos -= resetPoint;\n")
                new_lines.append("          svcGrid.scrollLeft = scrollPos;\n")
            new_lines.append("        } else {\n")
            new_lines.append("          scrollPos = svcGrid.scrollLeft;\n")
            new_lines.append("          if (svcGrid.style.scrollSnapType === 'none') svcGrid.style.scrollSnapType = '';\n")
            new_lines.append("        }\n")
            new_lines.append("        requestAnimationFrame(step);\n")
            new_lines.append("      }\n")
            new_lines.append("      requestAnimationFrame(step);\n")
            new_lines.append("    }\n")
        
        # Skip the original script lines until we hit the end of the if(svcGrid) block
        if in_script:
            if 'requestAnimationFrame(step);' in line or 'requestAnimationFrame(linearScroller);' in line:
                in_script = False
            continue
        
        new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Cleaned up marquee logic in index.html")

if __name__ == "__main__":
    final_sanitize('index.html')
    final_sanitize('service-data.js')
    final_sanitize('service-details.html')
    final_sanitize('book-appointment.html')
    final_sanitize('404.html')
    # fix_marquee_logic() # I'll run this manually if needed, but sanitize is priority
