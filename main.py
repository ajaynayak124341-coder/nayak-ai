import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import google.generativeai as genai

app = FastAPI()

# Environment variable se API key nikalna
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_html(question="", solution="", selected_subject="Maths"):
    maths_active = "bg-blue-600 text-white" if selected_subject == "Maths" else "bg-slate-700 text-slate-300"
    reasoning_active = "bg-blue-600 text-white" if selected_subject == "Reasoning" else "bg-slate-700 text-slate-300"
    science_active = "bg-blue-600 text-white" if selected_subject == "Science" else "bg-slate-700 text-slate-300"
    gk_active = "bg-blue-600 text-white" if selected_subject == "GK / GS" else "bg-slate-700 text-slate-300"

    solution_html = ""
    if solution:
        solution_html = f"""
        <div class="mt-6 p-4 bg-slate-900 border border-slate-800 rounded-xl">
            <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Your Question:</h3>
            <p class="text-white mt-1 mb-4 text-sm font-medium">{question}</p>
            <h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Step-by-Step Breakdown:</h3>
            <div class="text-slate-200 whitespace-pre-line text-sm leading-relaxed">{solution}</div>
        </div>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nayak AI | Universal Solver</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-950 text-white min-h-screen font-sans">
        <div class="max-w-2xl mx-auto p-4">
            <div class="flex justify-between items-center border-b border-slate-800 pb-4 mb-6">
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-blue-400 flex items-center gap-2">
                        ⚡ NAYAK AI
                    </h1>
                    <p class="text-xs text-slate-400 uppercase tracking-widest">Universal Solver</p>
                </div>
                <div class="bg-emerald-950 border border-emerald-500/30 text-emerald-400 text-xs px-3 py-1.5 rounded-full flex items-center gap-2 font-medium">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    ENGINE ACTIVE
                </div>
            </div>

            <div class="bg-slate-900/50 border border-slate-800 p-5 rounded-2xl shadow-xl">
                <h2 class="text-lg font-semibold mb-1 text-slate-200">Ask Your Doubt</h2>
                <p class="text-xs text-slate-400 mb-4">Sawal likhein aur Nayak AI ka real step-by-step master solution dekhein.</p>
                
                <form method="POST" action="/" class="space-y-4">
                    <div class="flex flex-wrap gap-2">
                        <label class="cursor-pointer">
                            <input type="radio" name="subject" value="Maths" checked class="hidden" onchange="this.form.submit()">
                            <span class="px-3 py-1.5 text-xs rounded-lg font-medium transition {maths_active}">Maths</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="subject" value="Reasoning" class="hidden" onchange="this.form.submit()">
                            <span class="px-3 py-1.5 text-xs rounded-lg font-medium transition {reasoning_active}">Reasoning</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="subject" value="Science" class="hidden" onchange="this.form.submit()">
                            <span class="px-3 py-1.5 text-xs rounded-lg font-medium transition {science_active}">Science</span>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="subject" value="GK / GS" class="hidden" onchange="this.form.submit()">
                            <span class="px-3 py-1.5 text-xs rounded-lg font-medium transition {gk_active}">GK / GS</span>
                        </label>
                    </div>

                    <div>
                        <textarea name="question" rows="4" required
                            class="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 transition"
                            placeholder="Apna question yahan type karein ya paste karein...">{question}</textarea>
                    </div>

                    <button type="submit" 
                        class="w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-semibold py-3 px-4 rounded-xl text-sm tracking-wide shadow-lg shadow-blue-500/10 active:scale-[0.99] transition">
                        ✨ SOLVE WITH NAYAK AI
                    </button>
                </form>
            </div>

            {solution_html}

            <div class="text-center mt-8 pt-4 border-t border-slate-900 text-xs text-slate-600">
                Engine Framework Designed for Excellence • Powered by Ajay Nayak
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return generate_html()

@app.post("/", response_class=HTMLResponse)
async def solve_question(question: str = Form(...), subject: str = Form("Maths")):
    if not api_key:
        return generate_html(question, "Error: Environment Variable mein 'GEMINI_API_KEY' nahi mili.", subject)
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are NAYAK AI UNIVERSAL SOLVER, an expert exam tutor for Indian government competitive exams like SSC GD and RRB ALP.
        Solve the following student question clearly.
        
        Provide the answer using this exact structure:
        **STEP 1: IDENTIFIERS & CONCEPT**
        (Explain the formula or trick here)
        
        **STEP 2: CALCULATIONS & SOLUTION STEPS**
        (Neat step-by-step calculation here)
        
        **✨ Final Verified Answer**
        (Clear final short answer here)
        
        Question: {question}
        Subject: {subject}
        """
        response = model.generate_content(prompt)
        solution = response.text
    except Exception as e:
        solution = f"Error processing query: {str(e)}"
        
    return generate_html(question, solution, subject)
