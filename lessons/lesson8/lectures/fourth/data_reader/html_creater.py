from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(data, divece = 1):
    t, p, w = data
    style = 'style="fint-size:22px;'
    html = '<html>\n  <head></head>\n <body>\n'
    html += '     <p {}> Темпрература: {} c</p>\n'.format(style,t)
    html += '     <p {}> Скорость ветра : {} m</p>\n'.format(style,w)
    html += '     <p {}> Атмосферное давление : {} mmHg</p>\n'.format(style, w)
    html += ' </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)
    
    return html