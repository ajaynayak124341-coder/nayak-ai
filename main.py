import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from typing import Optional
import google.generativeai as genai

app = FastAPI()

api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NAYAK AI | Universal Solver</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-[#090d16] text-slate-100 min-h-screen font-sans antialiased">
    <div class="max-w-2xl mx-auto p-4 sm:p-6">
        
        <div class="flex justify-between items-center border-b border-slate-800/60 pb-5 mb-6">
            <div class="flex items-center gap-3">
                <div class="bg-blue-600 p-2.5 rounded-xl shadow-lg shadow-blue-500/20">
                    <i class="fa-solid fa-bolt text-white text-lg"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-white flex items-center gap-2">
                        NAYAK AI
                    </h1>
                    <p class="text-[10px] text-blue-400 font-bold uppercase tracking-widest">Universal Solver</p>
                </div>
            </div>
            <div class="bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 text-xs px-3.5 py-1.5 rounded-full flex items-center gap-2 font-semibold">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                ENGINE ACTIVE
            </div>
        </div>

        <div class="bg-[#111827]/60 border border-slate-800/80 backdrop-blur-xl p-5 rounded-2xl shadow-2xl">
            <form method="POST" action="/" class="space-y-5">
                
                <div>
                    <label class="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2.5">Select Subject</label>
                    <div class="grid grid-cols-4 gap-2">
                        <label class="cursor-pointer text-center">
                            <input type="radio" name="subject" value="Maths" CHOSEN_MATHS class="hidden">
                            <span class="block py-2 text-xs rounded-xl font-bold transition border border-transparent CLASS_MATHS">MATHS</span>
                        </label>
                        <label class="cursor-pointer text-center">
                            <input type="radio" name="subject" value="Reasoning" CHOSEN_REASONING class="hidden">
                            <span class="block py-2 text-xs rounded-xl font-bold transition border border-transparent CLASS_REASONING">REASONING</span>
                        </label>
                        <label class="cursor-pointer text-center">
                            <input type="radio" name="subject" value="Science" CHOSEN_SCIENCE class="hidden">
                            <span class="block py-2 text-xs rounded-xl font-bold transition border border-transparent CLASS_SCIENCE">SCIENCE</span>
                        </label>
                        <label class="cursor-pointer text-center">
                            <input type="radio" name="subject" value="GK / GS" CHOSEN_GK class="hidden">
                            <span class="block py-2 text-xs rounded-xl font-bold transition border border-transparent CLASS_GK">GK / GS</span>
                        </label>
                    </div>
                </div>

                <div>
                    <label class="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">Your Question / Doubt</label>
                    <textarea name="question" rows="4" required
                        class="w-full bg-[#090d16] border border-slate-800 rounded-xl p-3.5 text-sm text-white placeholder-slate-600 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition shadow-inner"
                        placeholder="Apna question yahan type karein ya paste karein...">VAL_QUESTION</textarea>
                </div>

                <button type="submit" 
                    class="w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-bold py-3.5 px-4 rounded-xl text-xs tracking-wider uppercase shadow-lg shadow-blue-500/10 active:scale-[0.99] transition flex items-center justify-center gap-2">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> SOLVE WITH NAYAK AI
                </button>
            </form>
        </div>

        VAL_SOLUTION_HTML

        <div class="text-center mt-12 pt-5 border-t border-slate-900 text-[11px] text-slate-600 tracking-wide">
            Engine Framework Designed for Excellence • Powered by Ajay Nayak
        </div>
    </div>
</body>
</html>
"""

SOLUTION_TEMPLATE = """
<div class="mt-6 space-y-4">
    <div class="p-5 bg-[#111827]/40 border border-slate-800/60 rounded-2xl shadow-xl">
        <h3 class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1.5 flex items-center gap-1.5">
            <i class="fa-regular fa-circle-question text-slate-500"></i> Your Question:
        </h3>
        <p class="text-white text-sm font-semibold leading-relaxed bg-[#090d16]/50 p-3 rounded-xl border border-slate-800/40">VAL_Q</p>
        
        <h3 class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-5 mb-3 flex items-center gap-1.5">
            <i class="fa-solid fa-layer-group text-blue-400"></i> Step-by-Step Breakdown:
        </h3>
        
        <div class="text-slate-200 text-sm leading-relaxed space-y-4">
            VAL_ANS
        </div>
    </div>
</div>
"""

def get_response(question="", solution="", subject="Maths"):
    html = HTML_TEMPLATE
    
    active_style = "bg-blue-600 text-white shadow-lg shadow-blue-500/10 border-blue-500"
    inactive_style = "bg-slate-900 text-slate-400 border-slate-800/80 hover:bg-slate-800/50"
    
    if subject == "Maths":
        html = html.replace("CLASS_MATHS", active_style).replace("CHOSEN_MATHS", "checked")
    else:
        html = html.replace("CLASS_MATHS", inactive_style).replace("CHOSEN_MATHS", "")
        
    if subject == "Reasoning":
        html = html.replace("CLASS_REASONING", active_style).replace("CHOSEN_REASONING", "checked")
    else:
        html = html.replace("CLASS_REASONING", inactive_style).replace("CHOSEN_REASONING", "")
        
    if subject == "Science":
        html = html.replace("CLASS_SCIENCE", active_style).replace("CHOSEN_SCIENCE", "checked")
    else:
        html = html.replace("CLASS_SCIENCE", inactive_style).replace("CHOSEN_SCIENCE", "")
        
    if subject == "GK / GS":
        html = html.replace("CLASS_GK", active_style).replace("CHOSEN_GK", "checked")
    else:
        html = html.replace("CLASS_GK", inactive_style).replace("CHOSEN_GK", "")
    
    html = html.replace("VAL_QUESTION", question)
    
    if solution:
        sol_html = SOLUTION_TEMPLATE.replace("VAL_Q", question).replace("VAL_ANS", solution.replace("\\n", "<br>"))
        html = html.replace("VAL_SOLUTION_HTML", sol_html)
    else:
        html = html.replace("VAL_SOLUTION_HTML", "")
        
    return html

@app.get("/", response_class=HTMLResponse)
async def home():
    return get_response()

@app.post("/", response_class=HTMLResponse)
async def solve(question: Optional[str] = Form(None), subject: str = Form("Maths")):
    if not question:
        return get_response("", "", subject)
        
    if not api_key:
        return get_response(question, "Error: GEMINI_API_KEY set nahi hai.", subject)
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Subject: " + subject + "\\nQuestion: " + question + "\\n\\nSolve this step-by-step beautifully in Hinglish for an exam student."
        response = model.generate_content(prompt)
        solution = response.text
    except Exception as e:
        solution = "Error: " + str(e)
        
    return get_response(question, solution, subject)
