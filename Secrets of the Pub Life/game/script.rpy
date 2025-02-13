# prologue
label start:

    play audio prologue_voice
    $ renpy.movie_cutscene("video/prologue.webm", delay=10, stop_music=False)

    return
