# Висновки щодо швидкостей алгоритмів


### Таблиця результатів

| Текст  | Підрядок                   | Боєра-Мура (с) | Кнута-Морріса-Пратта (с) | Рабіна-Карпа (с) |
|--------|----------------------------|----------------|--------------------------|------------------|
| text1  | алгоритм пошуку            | 0.0105065      | 0.145235                 | 0.202948         |
| text1  | вигаданий підрядок         | 0.0089071      | 0.146435                 | 0.202019         |
| text1  | рекомендаційна система     | 0.0079887      | 0.150961                 | 0.212555         |
| text1  | незнайомий підрядок        | 0.0089627      | 0.147779                 | 0.206643         |
| text2  | алгоритм пошуку            | 0.0146387      | 0.1924                   | 0.266895         |
| text2  | вигаданий підрядок         | 0.0120227      | 0.191332                 | 0.266771         |
| text2  | рекомендаційна система     | 0.009831       | 0.19164                  | 0.264224         |
| text2  | незнайомий підрядок        | 0.0110711      | 0.186555                 | 0.268252         |


## В цілому
- **Алгоритм Боєра-Мура:** Середній час виконання склав 0.0105065 секунд.
- **Алгоритм Кнута-Морріса-Пратта:** Середній час виконання склав 0.152558 секунд.
- **Алгоритм Рабіна-Карпа:** Середній час виконання склав 0.21813375 секунд.
- **Загальний висновок:** В цілому, найшвидшим алгоритмом є алгоритм Боєра-Мура з середнім часом виконання 0.0105065 секунд.

### Загальні висновки

Алгоритм Боєра-Мура показав найкращу ефективність у всіх випадках для обох текстів, як для існуючих підрядків, так і для вигаданих. Він є найшвидшим серед трьох алгоритмів, що були протестовані (Кнута-Морріса-Пратта та Рабіна-Карпа).

## Рекомендації

Виходячи з результатів, алгоритм Боєра-Мура рекомендований для використання у завданнях пошуку підрядка в текстах, оскільки він показав найкращі результати за швидкістю виконання у всіх протестованих випадках.