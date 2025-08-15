# 🦈 Monster Shark Catch Fish Game

A web-based version of the classic Monster Shark Catch Fish game, converted from Python Pygame to HTML5 Canvas and JavaScript for web deployment.

## 🎮 Game Description

Control a shark and catch fish to score points! The game features:
- **Shark Movement**: Use arrow keys to control the shark
- **Fish Catching**: Position the shark's mouth to catch fish
- **Scoring System**: Earn points for each fish caught
- **Game Over**: Game ends after missing 100 fish
- **Restart**: Press 'R' to restart after game over

## 🚀 Quick Start

### Local Development
1. Clone the repository
2. Install dependencies: `npm install`
3. Start local server: `npm start`
4. Open browser to `http://localhost:3000`

### Vercel Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `npm run deploy`
3. Follow the prompts to complete deployment

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Graphics**: HTML5 Canvas API
- **Audio**: Web Audio API
- **Deployment**: Vercel (Static Site Hosting)
- **Original**: Python Pygame (converted from)

## 📁 Project Structure

```
monster-shark-game/
├── index.html          # Main HTML file
├── game.js            # Game logic and mechanics
├── vercel.json        # Vercel deployment configuration
├── package.json       # Project dependencies and scripts
├── README.md          # Project documentation
└── assets/            # Game assets (images, sounds)
    ├── shark.png      # Shark character sprite
    ├── fish.png       # Fish character sprite
    ├── background.png # Game background image
    ├── catch.wav      # Catch sound effect
    └── gameover.wav   # Game over sound effect
```

## 🎯 Game Controls

- **Arrow Keys**: Move shark in all directions
- **R Key**: Restart game (when game over)

## 🔧 Game Features

### Core Mechanics
- **Player Movement**: Smooth shark movement with boundary detection
- **Fish AI**: Fish move across screen and respawn when missed
- **Collision Detection**: Precise mouth area collision for fish catching
- **Score Tracking**: Real-time score and missed fish counter

### Audio System
- **Catch Sound**: High-pitched beep when fish is caught
- **Game Over Sound**: Low-pitched beep when game ends
- **Fallback**: Generated sounds using Web Audio API if audio files fail

### Visual Elements
- **Responsive Design**: Works on various screen sizes
- **Modern UI**: Clean, attractive interface with gradients
- **Fallback Graphics**: Placeholder shapes if images fail to load
- **Smooth Animation**: 60 FPS game loop using requestAnimationFrame

## 🚀 Deployment

### Vercel (Recommended)
1. **Automatic Deployment**: Push to GitHub and connect to Vercel
2. **Manual Deployment**: Use `vercel --prod` command
3. **Custom Domain**: Configure in Vercel dashboard

### Other Platforms
- **Netlify**: Drag and drop the project folder
- **GitHub Pages**: Push to `gh-pages` branch
- **Firebase Hosting**: Use Firebase CLI to deploy

## 🧪 Testing

### Local Testing
- Use `npm start` for local development server
- Test in multiple browsers (Chrome, Firefox, Safari, Edge)
- Test responsive design on different screen sizes

### Browser Compatibility
- **Modern Browsers**: Full support (Chrome 60+, Firefox 55+, Safari 12+)
- **Mobile Browsers**: Touch-friendly controls (future enhancement)
- **Fallbacks**: Graceful degradation for older browsers

## 🔮 Future Enhancements

- [ ] Mobile touch controls
- [ ] Power-ups and special fish
- [ ] Multiple difficulty levels
- [ ] High score leaderboard
- [ ] Sound effects toggle
- [ ] Particle effects
- [ ] Progressive Web App (PWA) support

## 🐛 Troubleshooting

### Common Issues
1. **Images not loading**: Check asset paths and file permissions
2. **Audio not working**: Ensure browser supports Web Audio API
3. **Game not starting**: Check browser console for JavaScript errors
4. **Deployment issues**: Verify Vercel configuration and build settings

### Debug Mode
- Open browser console (F12) for detailed error messages
- Check network tab for failed asset requests
- Verify all files are properly uploaded to deployment platform

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Original Python Pygame version
- HTML5 Canvas API documentation
- Web Audio API examples
- Vercel deployment platform

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review browser console for errors
3. Create an issue in the repository
4. Contact the development team

---

**Happy Gaming! 🎮✨**
