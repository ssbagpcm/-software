import webview

webview.create_window(
    title='',
    url='sguibeta.html',
    resizable=True,
    fullscreen=True,
    min_size=(350, 350),
    frameless=True,
    easy_drag=True,
    shadow=True,
    focus=True,
    maximized=True,
    background_color='#000000',
    draggable=True,
)

webview.start()
