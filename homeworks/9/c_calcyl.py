

# модуль для расчетов операций

import cmath
def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = c_calc(j)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()