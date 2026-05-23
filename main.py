from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nayak AI | Universal Question Solver</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white min-h-screen flex flex-col justify-between font-sans selection:bg-cyan-500 selection:text-slate-950">

        <header class="border-b border-slate-800/80 bg-slate-900/40 backdrop-blur-xl sticky top-0 z-50 px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-gradient-to-r from-cyan-500 to-blue-600 p-2.5 rounded-xl shadow-lg shadow-cyan-500/20">
                    <i class="fas fa-bolt text-lg text-slate-950"></i>
                </div>
                <div>
                    <span class="text-xl font-black tracking-wider bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400 bg-clip-text text-transparent">NAYAK AI</span>
                    <span class="text-[10px] block font-bold text-slate-500 tracking-widest uppercase -mt-1">Universal Solver</span>
                </div>
            </div>
            
            <div class="flex items-center space-x-4">
                <div class="hidden sm:flex items-center bg-slate-800/50 border border-slate-700/60 rounded-xl p-1 text-xs font-semibold text-slate-400">
                    <span class="px-3 py-1 bg-slate-900 text-cyan-400 rounded-lg shadow-sm">v1.0 Live</span>
                    <span class="px-3 py-1">Secure</span>
                </div>
                <div class="flex items-center space-x-2 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1.5 rounded-full">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Engine Active</span>
                </div>
            </div>
        </header>

        <main class="max-w-7xl mx-auto w-full px-4 sm:px-6 py-8 flex-grow grid grid-cols-1 lg:grid-cols-12 gap-8 my-auto">
            
            <section class="lg:col-span-5 flex flex-col space-y-6">
                <div class="bg-slate-900/50 border border-slate-800/80 rounded-2xl p-6 backdrop-blur-md shadow-xl flex flex-col justify-between h-full">
                    <div class="space-y-5">
                        <div>
                            <h2 class="text-xl font-extrabold tracking-tight text-slate-100">Ask Your Doubt</h2>
                            <p class="text-slate-400 text-xs mt-1">Koi bhi sawal likhein ya photo upload karein, Nayak AI turant solution nikalega.</p>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                            <button onclick="setSubject('Maths')" id="tab-Maths" class="subject-tab py-2.5 px-2 rounded-xl border border-cyan-500/30 bg-cyan-500/10 text-cyan-400 font-bold text-xs flex flex-col items-center justify-center space-y-1 transition duration-200 hover:border-cyan-400">
                                <i class="fas fa-calculator text-sm"></i>
                                <span>Maths</span>
                            </button>
                            <button onclick="setSubject('Reasoning')" id="tab-Reasoning" class="subject-tab py-2.5 px-2 rounded-xl border border-slate-800 bg-slate-950/40 text-slate-400 font-bold text-xs flex flex-col items-center justify-center space-y-1 transition duration-200 hover:border-slate-700">
                                <i class="fas fa-brain text-sm"></i>
                                <span>Reasoning</span>
                            </button>
                            <button onclick="setSubject('Science')" id="tab-Science" class="subject-tab py-2.5 px-2 rounded-xl border border-slate-800 bg-slate-950/40 text-slate-400 font-bold text-xs flex flex-col items-center justify-center space-y-1 transition duration-200 hover:border-slate-700">
                                <i class="fas fa-flask text-sm"></i>
                                <span>Science</span>
                            </button>
                            <button onclick="setSubject('GK/GS')" id="tab-GK" class="subject-tab py-2.5 px-2 rounded-xl border border-slate-800 bg-slate-950/40 text-slate-400 font-bold text-xs flex flex-col items-center justify-center space-y-1 transition duration-200 hover:border-slate-700">
                                <i class="fas fa-book text-sm"></i>
                                <span>GK / GS</span>
                            </button>
                        </div>

                        <div class="relative">
                            <textarea id="questionInput" rows="6" class="w-full bg-slate-950/60 border border-slate-800 focus:border-cyan-500/50 rounded-xl p-4 text-slate-200 placeholder-slate-600 focus:outline-none focus:ring-1 focus:ring-cyan-500/30 text-sm resize-none transition" placeholder="Apna question yahan type karein ya paste karein..."></textarea>
                            
                            <div class="absolute bottom-3 left-3 flex items-center space-x-2">
                                <label class="cursor-pointer bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-400 hover:text-slate-200 px-3 py-1.5 rounded-lg text-xs font-medium flex items-center space-x-1.5 transition">
                                    <i class="fas fa-camera text-cyan-400"></i>
                                    <span>Upload Photo</span>
                                    <input type="file" accept="image/*" class="hidden" onchange="simulateUpload(event)">
                                </label>
                                <span id="fileStatus" class="text-[11px] text-emerald-400 font-semibold hidden"><i class="fas fa-check-circle mr-1"></i> Image Loaded</span>
                            </div>
                        </div>
                    </div>

                    <button onclick="generateSolution()" class="w-full mt-6 bg-gradient-to-r from-cyan-500 via-blue-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-slate-950 font-black text-sm uppercase tracking-wider py-4 rounded-xl shadow-lg shadow-cyan-500/10 hover:shadow-cyan-500/20 active:scale-[0.99] transition duration-150 flex items-center justify-center space-x-2">
                        <i class="fas fa-wand-magic-sparkles text-base"></i>
                        <span>Solve with Nayak AI</span>
                    </button>
                </div>
            </section>

            <section class="lg:col-span-7 flex flex-col h-full">
                <div id="solutionContainer" class="bg-slate-900/30 border border-slate-800/60 rounded-2xl p-6 backdrop-blur-md shadow-xl flex flex-col justify-center items-center text-center min-h-[400px] lg:h-full transition-all duration-300">
                    
                    <div id="placeholderState" class="space-y-4 max-w-sm">
                        <div class="w-16 h-16 bg-slate-900 border border-slate-800 rounded-2xl flex items-center justify-center mx-auto text-slate-600 text-xl shadow-inner">
                            <i class="fas fa-terminal animate-pulse text-cyan-500/40"></i>
                        </div>
                        <div>
                            <h3 class="text-base font-bold text-slate-300">Awaiting Input</h3>
                            <p class="text-slate-500 text-xs mt-1">Left panel mein sawal poochiye. Nayak AI ka step-by-step master solution yahan dikhega.</p>
                        </div>
                    </div>

                    <div id="solutionState" class="w-full text-left space-y-5 hidden animate-fade-in">
                        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
                            <div class="flex items-center space-x-2">
                                <span id="outputBadge" class="bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-[11px] font-black uppercase tracking-wider px-2.5 py-1 rounded-md">MATHS</span>
                                <span class="text-slate-500 text-xs font-medium"><i class="far fa-clock mr-1"></i> Processed in 0.4s</span>
                            </div>
                            <button class="text-slate-500 hover:text-slate-300 text-xs flex items-center space-x-1 border border-slate-800 px-2.5 py-1 rounded-lg hover:bg-slate-900 transition">
                                <i class="far fa-bookmark"></i>
                                <span>Save Doubt</span>
                            </button>
                        </div>

                        <div class="space-y-4">
                            <div class="bg-slate-950/40 border border-slate-800/80 p-4 rounded-xl">
                                <h4 class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Your Question:</h4>
                                <p id="copiedQuestion" class="text-slate-200 text-sm font-medium italic"></p>
                            </div>

                            <div class="space-y-3">
                                <h4 class="text-xs font-bold text-slate-500 uppercase tracking-wider pl-1">Step-by-Step Breakdown:</h4>
                                
                                <div class="bg-slate-900/60 border border-slate-800/50 p-4 rounded-xl border-l-2 border-l-cyan-500">
                                    <div class="text-xs font-bold text-cyan-400 uppercase tracking-wide mb-1">Step 1: Identifiers & Concept</div>
                                    <p class="text-slate-300 text-sm leading-relaxed">Sawal ke patterns ko scan karne ke baad, required core formula apply kiya gaya hai. Concept clear hai.</p>
                                </div>

                                <div class="bg-slate-900/60 border border-slate-800/50 p-4 rounded-xl border-l-2 border-l-indigo-500">
                                    <div class="text-xs font-bold text-indigo-400 uppercase tracking-wide mb-1">Step 2: Core Calculation / Logical Path</div>
                                    <p class="text-slate-300 text-sm leading-relaxed">Nayak Engine shortcut tricks aur standard methodology dono ko combine karke final values ko calculate kar raha hai.</p>
                                </div>

                                <div class="bg-slate-950/80 border border-emerald-500/20 p-4 rounded-xl border-l-2 border-l-emerald-500 bg-gradient-to-r from-emerald-500/5 to-transparent">
                                    <div class="text-xs font-bold text-emerald-400 uppercase tracking-wide mb-1">Final Verified Answer</div>
                                    <p class="text-slate-100 font-extrabold text-base">Sawal ka sateek aur sahi uttar taiyar hai! Aap is method se exam mein time bacha sakte hain.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </section>

        </main>

        <footer class="w-full text-center py-5 border-t border-slate-900/60 text-slate-500 text-xs bg-slate-950/30">
            <p class="tracking-wide">Engine Framework Designed for Excellence • Powered by <span class="text-slate-300 font-semibold">Nayak AI Core v1.0</span></p>
        </footer>

        <script>
            let currentSubject = 'Maths';

            function setSubject(subject) {
                currentSubject = subject;
                document.querySelectorAll('.subject-tab').forEach(tab => {
                    tab.classList.remove('border-cyan-500/30', 'bg-cyan-500/10', 'text-cyan-400');
                    tab.classList.add('border-slate-800', 'bg-slate-950/40', 'text-slate-400');
                });
                
                const activeTab = document.getElementById('tab-' + (subject === 'GK/GS' ? 'GK' : subject));
                if(activeTab) {
                    activeTab.classList.remove('border-slate-800', 'bg-slate-950/40', 'text-slate-400');
                    activeTab.classList.add('border-cyan-500/30', 'bg-cyan-500/10', 'text-cyan-400');
                }
            }

            function simulateUpload(event) {
                if(event.target.files.length > 0) {
                    document.getElementById('fileStatus').classList.remove('hidden');
                    if(document.getElementById('questionInput').value.trim() === "") {
                        document.getElementById('questionInput').value = "[Image Attached: Question from file]";
                    }
                }
            }

            function generateSolution() {
                const queryText = document.getElementById('questionInput').value.trim();
                if(queryText === "") {
                    alert("Pehle input box mein koi sawal likhein ya image upload karein!");
                    return;
                }

                // Switch UI visibility smoothly
                document.getElementById('placeholderState').classList.add('hidden');
                document.getElementById('solutionContainer').classList.remove('justify-center', 'items-center', 'text-center');
                document.getElementById('solutionState').classList.remove('hidden');
                document.getElementById('outputBadge').innerText = currentSubject.toUpperCase();
                document.getElementById('copiedQuestion').innerText = queryText;
            }
        </script>
    </body>
    </html>
    """
    return html_content
