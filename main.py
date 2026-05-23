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
        <title>Nayak AI | Cloud Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white min-h-screen flex flex-col justify-between font-sans">

        <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50 px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-cyan-500 p-2 rounded-xl shadow-lg shadow-cyan-500/30 animate-pulse">
                    <i class="fas fa-brain text-xl text-slate-950"></i>
                </div>
                <span class="text-xl font-black tracking-wider bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">NAYAK AI</span>
            </div>
            <div class="flex items-center space-x-2 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1.5 rounded-full">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
                <span class="text-xs font-semibold text-emerald-400 tracking-wide uppercase">Server Live</span>
            </div>
        </header>

        <main class="max-w-4xl mx-auto px-6 py-12 flex flex-col justify-center items-center my-auto text-center space-y-8">
            <div class="space-y-4">
                <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight">
                    Welcome to <span class="bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-500 bg-clip-text text-transparent">Nayak AI Control Center</span>
                </h1>
                <p class="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto font-light">
                    Aapka personal Gemini AI backend cloud par kamyabi se deploy ho chuka hai aur dhoom machane ke liye taiyar hai!
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-3xl pt-6">
                <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-2xl text-left hover:border-cyan-500/40 transition duration-300 backdrop-blur-sm group">
                    <div class="text-cyan-400 text-2xl mb-3 group-hover:scale-110 transition duration-300"><i class="fas fa-server"></i></div>
                    <h3 class="font-bold text-slate-200 text-base">Host Platform</h3>
                    <p class="text-slate-400 text-sm mt-1">Render Cloud (Docker Container)</p>
                </div>
                <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-2xl text-left hover:border-blue-500/40 transition duration-300 backdrop-blur-sm group">
                    <div class="text-blue-400 text-2xl mb-3 group-hover:scale-110 transition duration-300"><i class="fas fa-microchip"></i></div>
                    <h3 class="font-bold text-slate-200 text-base">Core Engine</h3>
                    <p class="text-slate-400 text-sm mt-1">FastAPI + Google Gemini API</p>
                </div>
                <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-2xl text-left hover:border-indigo-500/40 transition duration-300 backdrop-blur-sm group">
                    <div class="text-indigo-400 text-2xl mb-3 group-hover:scale-110 transition duration-300"><i class="fas fa-code-branch"></i></div>
                    <h3 class="font-bold text-slate-200 text-base">CI/CD Pipeline</h3>
                    <p class="text-slate-400 text-sm mt-1">GitHub Auto Deployment</p>
                </div>
            </div>

            <div class="pt-4">
                <div class="inline-flex items-center space-x-2 bg-slate-800/80 border border-slate-700/80 text-slate-300 px-5 py-3 rounded-xl font-medium shadow-md">
                    <i class="fas fa-terminal text-cyan-400 mr-2"></i>
                    <span>Status: <span class="text-emerald-400 font-bold">Perfect & Active</span></span>
                </div>
            </div>
        </main>

        <footer class="w-full text-center py-6 border-t border-slate-900/60 text-slate-500 text-sm bg-slate-950/40">
            <p>Made with <i class="fas fa-heart text-red-500 mx-1"></i> by <span class="text-slate-300 font-semibold">Ajay Nayak</span></p>
        </footer>

    </body>
    </html>
    """
    return html_content
