from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

def generate_reel(prompt, output_path):
    txt = TextClip(prompt, fontsize=70, color='white', size=(1080, 1920), method='caption')
    txt = txt.set_duration(5).set_position('center')
    bg = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=5)
    final = CompositeVideoClip([bg, txt])
    final.write_videofile(output_path, fps=24)
