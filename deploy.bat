@echo off
echo 🦈 Deploying Monster Shark Game to Vercel...

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Vercel CLI not found. Installing...
    npm install -g vercel
)

REM Check if we're in the right directory
if not exist "index.html" (
    echo ❌ Error: Please run this script from the project root directory
    pause
    exit /b 1
)

if not exist "game.js" (
    echo ❌ Error: Please run this script from the project root directory
    pause
    exit /b 1
)

REM Build check (no build step needed for static site)
echo ✅ Build check passed (static site)

REM Deploy to Vercel
echo 🚀 Deploying to Vercel...
vercel --prod

echo 🎉 Deployment complete!
echo 🌐 Your game should now be live on Vercel!
echo 📱 Check your Vercel dashboard for the live URL
pause
