#!/bin/bash

# Monster Shark Game Deployment Script
echo "🦈 Deploying Monster Shark Game to Vercel..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Check if we're in the right directory
if [ ! -f "index.html" ] || [ ! -f "game.js" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Build check (no build step needed for static site)
echo "✅ Build check passed (static site)"

# Deploy to Vercel
echo "🚀 Deploying to Vercel..."
vercel --prod

echo "🎉 Deployment complete!"
echo "🌐 Your game should now be live on Vercel!"
echo "📱 Check your Vercel dashboard for the live URL"
