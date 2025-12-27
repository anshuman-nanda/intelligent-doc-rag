# Placeholder for Documentation Images

This directory contains images and GIFs used in the README and documentation.

## Current Placeholders

- `ingestion-demo.gif` - Demo of document ingestion process
- `search-demo.gif` - Demo of semantic search in action
- `web-interface.png` - Screenshot of the web interface

## Contributing Images

When adding real images/GIFs to replace these placeholders:

1. **Format**: Use PNG for screenshots, GIF or MP4 for animations
2. **Size**: Keep file sizes under 5MB when possible
3. **Resolution**: Minimum 1280x720 for screenshots
4. **Optimization**: Use tools like TinyPNG or Gifski to optimize

## Creating Demo GIFs

Recommended tools:
- **macOS**: QuickTime + Gifski
- **Windows**: ScreenToGif
- **Linux**: Peek or SimpleScreenRecorder + ffmpeg
- **Cross-platform**: OBS Studio + ffmpeg

### Example conversion command:
```bash
ffmpeg -i input.mp4 -vf "fps=10,scale=1280:-1:flags=lanczos" output.gif
```
