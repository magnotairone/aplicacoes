---
output: html_document
editor_options: 
  chunk_output_type: console
---
# Introdução à Classificação

Vamos entender como os modelos de Data Science tomam decisões binárias (Sim/Não, Fraude/Legal, Compra/Não Compra, 0/1).

### Terminologia Básica {.unnumbered}

- **Target ($Y$):** O fenômeno que queremos prever (ex: Inadimplência).
- **Features ($X$):** As características que usamos para explicar o fenômeno (ex: Score de crédito, renda).
- **O Modelo ($f$):** A regra de decisão que conecta as features ao resultado esperado.

Um modelo preditivo é uma classe de funções $f$ que tenta se aproximar $X$ de $Y$, ou seja, 
$$Y = f(X).$$

## Avaliação de performance de um modelo de classificação

Antes de aprender a treinar um modelo, vamos considerar que o modelo foi treinado e vamos avaliar sua performance.


<!-- Para entender as métricas, vamos considerar dois modelos hipotéticos. O **Modelo A** é mais agressivo (quer capturar tudo), enquanto o **Modelo B** é conservador (só aponta quando tem muita certeza). -->

Para entender as métricas, vamos considerar dois modelos hipotéticos. O **Modelo A** e o **Modelo B**. A predição da probabilidade do evento de interesse (target ser `1`) calculada por cada um dos modelos está na tabela abaixo.


::: {.cell}
::: {.cell-output-display}
`````{=html}
<div style="border: 1px solid #ddd; padding: 0px; overflow-y: scroll; height:300px; overflow-x: scroll; width:100%; "><table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:right;position: sticky; top:0; background-color: #FFFFFF;"> id </th>
   <th style="text-align:right;position: sticky; top:0; background-color: #FFFFFF;"> real </th>
   <th style="text-align:right;position: sticky; top:0; background-color: #FFFFFF;"> prob_mod_A </th>
   <th style="text-align:right;position: sticky; top:0; background-color: #FFFFFF;"> prob_mod_B </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5266653 </td>
   <td style="text-align:right;"> 0.1466474 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 2 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5059166 </td>
   <td style="text-align:right;"> 0.0110548 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 3 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5703827 </td>
   <td style="text-align:right;"> 0.2066902 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 4 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5384055 </td>
   <td style="text-align:right;"> 0.3739403 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 5 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9284680 </td>
   <td style="text-align:right;"> 0.0974194 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 6 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1821725 </td>
   <td style="text-align:right;"> 0.0835612 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 7 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1899199 </td>
   <td style="text-align:right;"> 0.0204241 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 8 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9663012 </td>
   <td style="text-align:right;"> 0.2403884 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 9 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2845407 </td>
   <td style="text-align:right;"> 0.0049430 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 10 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5016221 </td>
   <td style="text-align:right;"> 0.0436003 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 11 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7335471 </td>
   <td style="text-align:right;"> 0.5272531 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 12 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3053173 </td>
   <td style="text-align:right;"> 0.0923066 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 13 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1876045 </td>
   <td style="text-align:right;"> 0.0662686 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 14 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4577943 </td>
   <td style="text-align:right;"> 0.2599282 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 15 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2223173 </td>
   <td style="text-align:right;"> 0.0893167 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 16 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8404193 </td>
   <td style="text-align:right;"> 0.7015037 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 17 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3850288 </td>
   <td style="text-align:right;"> 0.0657415 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 18 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7216431 </td>
   <td style="text-align:right;"> 0.0596303 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 19 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2268990 </td>
   <td style="text-align:right;"> 0.0205996 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 20 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7500680 </td>
   <td style="text-align:right;"> 0.2003447 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 21 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4795943 </td>
   <td style="text-align:right;"> 0.2178168 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 22 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1940075 </td>
   <td style="text-align:right;"> 0.1954568 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 23 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0918197 </td>
   <td style="text-align:right;"> 0.0303322 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 24 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7667997 </td>
   <td style="text-align:right;"> 0.0225454 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 25 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2536493 </td>
   <td style="text-align:right;"> 0.0534286 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 26 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2132733 </td>
   <td style="text-align:right;"> 0.0592550 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 27 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6349615 </td>
   <td style="text-align:right;"> 0.0239998 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 28 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1373349 </td>
   <td style="text-align:right;"> 0.0661344 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 29 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3800534 </td>
   <td style="text-align:right;"> 0.1165600 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 30 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0983941 </td>
   <td style="text-align:right;"> 0.0200849 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 31 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8058449 </td>
   <td style="text-align:right;"> 0.4942391 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 32 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9205924 </td>
   <td style="text-align:right;"> 0.7724923 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 33 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5603363 </td>
   <td style="text-align:right;"> 0.1591484 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 34 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1839712 </td>
   <td style="text-align:right;"> 0.0513608 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 35 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0442348 </td>
   <td style="text-align:right;"> 0.0209925 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 36 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1040718 </td>
   <td style="text-align:right;"> 0.0506815 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 37 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5163154 </td>
   <td style="text-align:right;"> 0.2242917 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 38 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2305944 </td>
   <td style="text-align:right;"> 0.0253055 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 39 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0293241 </td>
   <td style="text-align:right;"> 0.0074456 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 40 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2507009 </td>
   <td style="text-align:right;"> 0.1180106 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 41 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6467690 </td>
   <td style="text-align:right;"> 0.0183882 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 42 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4335259 </td>
   <td style="text-align:right;"> 0.2894360 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 43 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1475454 </td>
   <td style="text-align:right;"> 0.1817755 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 44 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0684252 </td>
   <td style="text-align:right;"> 0.1295169 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 45 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1468277 </td>
   <td style="text-align:right;"> 0.0197985 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 46 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2927390 </td>
   <td style="text-align:right;"> 0.0849063 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 47 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4985272 </td>
   <td style="text-align:right;"> 0.0384018 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 48 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0407516 </td>
   <td style="text-align:right;"> 0.0220309 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 49 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5360576 </td>
   <td style="text-align:right;"> 0.0369337 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 50 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6611332 </td>
   <td style="text-align:right;"> 0.2114369 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 51 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4148202 </td>
   <td style="text-align:right;"> 0.0244914 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 52 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0598790 </td>
   <td style="text-align:right;"> 0.0399547 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 53 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1694696 </td>
   <td style="text-align:right;"> 0.0496681 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 54 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2035999 </td>
   <td style="text-align:right;"> 0.0836408 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 55 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5418839 </td>
   <td style="text-align:right;"> 0.4685883 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 56 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5374561 </td>
   <td style="text-align:right;"> 0.0725644 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 57 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3817822 </td>
   <td style="text-align:right;"> 0.0115650 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 58 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1927036 </td>
   <td style="text-align:right;"> 0.0034041 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 59 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8970755 </td>
   <td style="text-align:right;"> 0.1605151 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 60 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2785107 </td>
   <td style="text-align:right;"> 0.0143477 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 61 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1693680 </td>
   <td style="text-align:right;"> 0.0350236 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 62 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5082374 </td>
   <td style="text-align:right;"> 0.0966152 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 63 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6384087 </td>
   <td style="text-align:right;"> 0.1392930 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 64 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4958388 </td>
   <td style="text-align:right;"> 0.0043233 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 65 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4812649 </td>
   <td style="text-align:right;"> 0.2740592 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 66 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2000648 </td>
   <td style="text-align:right;"> 0.0566142 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 67 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8470241 </td>
   <td style="text-align:right;"> 0.3764576 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 68 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6451348 </td>
   <td style="text-align:right;"> 0.1779509 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 69 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2221399 </td>
   <td style="text-align:right;"> 0.2301823 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 70 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6038731 </td>
   <td style="text-align:right;"> 0.0428619 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 71 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1492508 </td>
   <td style="text-align:right;"> 0.1387198 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 72 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4288869 </td>
   <td style="text-align:right;"> 0.0264038 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 73 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1481011 </td>
   <td style="text-align:right;"> 0.2586787 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 74 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0867598 </td>
   <td style="text-align:right;"> 0.0240081 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 75 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3140416 </td>
   <td style="text-align:right;"> 0.0425682 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 76 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4971168 </td>
   <td style="text-align:right;"> 0.0081376 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 77 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0527453 </td>
   <td style="text-align:right;"> 0.2025258 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 78 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0959836 </td>
   <td style="text-align:right;"> 0.0506766 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 79 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7453542 </td>
   <td style="text-align:right;"> 0.0062909 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 80 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2059715 </td>
   <td style="text-align:right;"> 0.0678124 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 81 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3989130 </td>
   <td style="text-align:right;"> 0.0087009 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 82 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1908702 </td>
   <td style="text-align:right;"> 0.0004688 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 83 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2291735 </td>
   <td style="text-align:right;"> 0.0773382 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 84 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3036621 </td>
   <td style="text-align:right;"> 0.0821273 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 85 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2879334 </td>
   <td style="text-align:right;"> 0.1406030 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 86 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2483969 </td>
   <td style="text-align:right;"> 0.0925113 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 87 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7685659 </td>
   <td style="text-align:right;"> 0.1096753 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 88 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6014734 </td>
   <td style="text-align:right;"> 0.2591656 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 89 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8937466 </td>
   <td style="text-align:right;"> 0.2453573 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 90 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2529627 </td>
   <td style="text-align:right;"> 0.2778436 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 91 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5290680 </td>
   <td style="text-align:right;"> 0.0847351 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 92 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6083515 </td>
   <td style="text-align:right;"> 0.0105925 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 93 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1158564 </td>
   <td style="text-align:right;"> 0.3572270 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 94 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1087646 </td>
   <td style="text-align:right;"> 0.0820217 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 95 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4623510 </td>
   <td style="text-align:right;"> 0.0158401 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 96 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3151072 </td>
   <td style="text-align:right;"> 0.0455743 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 97 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2110198 </td>
   <td style="text-align:right;"> 0.1703938 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 98 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2151356 </td>
   <td style="text-align:right;"> 0.0582797 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 99 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1255112 </td>
   <td style="text-align:right;"> 0.0112903 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 100 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3041377 </td>
   <td style="text-align:right;"> 0.0124898 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 101 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3409711 </td>
   <td style="text-align:right;"> 0.0148688 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 102 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3299499 </td>
   <td style="text-align:right;"> 0.0680660 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 103 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2158597 </td>
   <td style="text-align:right;"> 0.0335702 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 104 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7175068 </td>
   <td style="text-align:right;"> 0.2332085 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 105 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3397399 </td>
   <td style="text-align:right;"> 0.0646018 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 106 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9858790 </td>
   <td style="text-align:right;"> 0.7635717 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 107 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7972175 </td>
   <td style="text-align:right;"> 0.3404882 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 108 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1153123 </td>
   <td style="text-align:right;"> 0.0788042 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 109 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1150458 </td>
   <td style="text-align:right;"> 0.1941952 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 110 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3078574 </td>
   <td style="text-align:right;"> 0.0647578 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 111 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9201054 </td>
   <td style="text-align:right;"> 0.3440811 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 112 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3814433 </td>
   <td style="text-align:right;"> 0.1816832 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 113 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5016740 </td>
   <td style="text-align:right;"> 0.0073409 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 114 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6769279 </td>
   <td style="text-align:right;"> 0.4567098 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 115 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2751695 </td>
   <td style="text-align:right;"> 0.0835300 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 116 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4809954 </td>
   <td style="text-align:right;"> 0.3275936 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 117 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2368716 </td>
   <td style="text-align:right;"> 0.0495029 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 118 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8831744 </td>
   <td style="text-align:right;"> 0.0920918 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 119 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3519601 </td>
   <td style="text-align:right;"> 0.0158350 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 120 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2737473 </td>
   <td style="text-align:right;"> 0.1460921 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 121 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1863470 </td>
   <td style="text-align:right;"> 0.0960247 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 122 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2585360 </td>
   <td style="text-align:right;"> 0.0090521 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 123 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4945868 </td>
   <td style="text-align:right;"> 0.0032522 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 124 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1351883 </td>
   <td style="text-align:right;"> 0.0981388 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 125 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0966623 </td>
   <td style="text-align:right;"> 0.0553465 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 126 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4310067 </td>
   <td style="text-align:right;"> 0.4455092 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 127 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3485294 </td>
   <td style="text-align:right;"> 0.1167269 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 128 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1643676 </td>
   <td style="text-align:right;"> 0.0187001 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 129 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4969284 </td>
   <td style="text-align:right;"> 0.1289645 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 130 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2595347 </td>
   <td style="text-align:right;"> 0.2056507 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 131 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1102104 </td>
   <td style="text-align:right;"> 0.0113160 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 132 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5699990 </td>
   <td style="text-align:right;"> 0.2039816 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 133 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6792228 </td>
   <td style="text-align:right;"> 0.2977282 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 134 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3816331 </td>
   <td style="text-align:right;"> 0.0733843 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 135 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3260824 </td>
   <td style="text-align:right;"> 0.0368393 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 136 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1710119 </td>
   <td style="text-align:right;"> 0.0078947 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 137 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5411158 </td>
   <td style="text-align:right;"> 0.3223017 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 138 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1159943 </td>
   <td style="text-align:right;"> 0.1132668 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 139 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9591654 </td>
   <td style="text-align:right;"> 0.1712768 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 140 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2770387 </td>
   <td style="text-align:right;"> 0.0850821 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 141 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2787786 </td>
   <td style="text-align:right;"> 0.0330486 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 142 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0996784 </td>
   <td style="text-align:right;"> 0.3249209 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 143 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3214911 </td>
   <td style="text-align:right;"> 0.0828674 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 144 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4759983 </td>
   <td style="text-align:right;"> 0.0152365 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 145 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4647713 </td>
   <td style="text-align:right;"> 0.1157301 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 146 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2835532 </td>
   <td style="text-align:right;"> 0.0168108 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 147 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1583783 </td>
   <td style="text-align:right;"> 0.1158770 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 148 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2726127 </td>
   <td style="text-align:right;"> 0.1005314 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 149 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3932962 </td>
   <td style="text-align:right;"> 0.0299165 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 150 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0350361 </td>
   <td style="text-align:right;"> 0.1156279 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 151 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7199862 </td>
   <td style="text-align:right;"> 0.2539506 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 152 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4075105 </td>
   <td style="text-align:right;"> 0.0048706 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 153 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2789820 </td>
   <td style="text-align:right;"> 0.1564739 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 154 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2821200 </td>
   <td style="text-align:right;"> 0.0001483 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 155 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2564157 </td>
   <td style="text-align:right;"> 0.1816861 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 156 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3403748 </td>
   <td style="text-align:right;"> 0.0789808 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 157 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1945506 </td>
   <td style="text-align:right;"> 0.0775331 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 158 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3449781 </td>
   <td style="text-align:right;"> 0.0430375 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 159 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1330390 </td>
   <td style="text-align:right;"> 0.1115755 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 160 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3278659 </td>
   <td style="text-align:right;"> 0.0247541 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 161 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5597158 </td>
   <td style="text-align:right;"> 0.0388404 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 162 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5390256 </td>
   <td style="text-align:right;"> 0.1972618 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 163 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1136290 </td>
   <td style="text-align:right;"> 0.1845918 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 164 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2969097 </td>
   <td style="text-align:right;"> 0.0164615 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 165 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4268209 </td>
   <td style="text-align:right;"> 0.3154443 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 166 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1162954 </td>
   <td style="text-align:right;"> 0.0399974 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 167 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6909630 </td>
   <td style="text-align:right;"> 0.1976487 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 168 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1202355 </td>
   <td style="text-align:right;"> 0.0583706 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 169 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3201085 </td>
   <td style="text-align:right;"> 0.1191381 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 170 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3173729 </td>
   <td style="text-align:right;"> 0.2325683 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 171 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3109251 </td>
   <td style="text-align:right;"> 0.1415014 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 172 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2450928 </td>
   <td style="text-align:right;"> 0.0842179 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 173 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7908077 </td>
   <td style="text-align:right;"> 0.5535966 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 174 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1206729 </td>
   <td style="text-align:right;"> 0.2981254 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 175 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0920874 </td>
   <td style="text-align:right;"> 0.0371983 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 176 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1712608 </td>
   <td style="text-align:right;"> 0.0461804 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 177 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2742769 </td>
   <td style="text-align:right;"> 0.2362455 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 178 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6026400 </td>
   <td style="text-align:right;"> 0.0973480 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 179 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4173363 </td>
   <td style="text-align:right;"> 0.3817622 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 180 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3546537 </td>
   <td style="text-align:right;"> 0.1268357 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 181 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8480256 </td>
   <td style="text-align:right;"> 0.0928470 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 182 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2390188 </td>
   <td style="text-align:right;"> 0.0563224 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 183 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2955187 </td>
   <td style="text-align:right;"> 0.0006213 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 184 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0808903 </td>
   <td style="text-align:right;"> 0.0264357 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 185 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3479056 </td>
   <td style="text-align:right;"> 0.1135253 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 186 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1895060 </td>
   <td style="text-align:right;"> 0.0424682 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 187 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3581540 </td>
   <td style="text-align:right;"> 0.0079903 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 188 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2208777 </td>
   <td style="text-align:right;"> 0.1410112 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 189 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8344097 </td>
   <td style="text-align:right;"> 0.4675791 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 190 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6896739 </td>
   <td style="text-align:right;"> 0.0561226 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 191 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2172737 </td>
   <td style="text-align:right;"> 0.1084421 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 192 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5562314 </td>
   <td style="text-align:right;"> 0.0837209 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 193 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6522283 </td>
   <td style="text-align:right;"> 0.2285563 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 194 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3811597 </td>
   <td style="text-align:right;"> 0.0944294 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 195 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6663639 </td>
   <td style="text-align:right;"> 0.3998170 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 196 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6714810 </td>
   <td style="text-align:right;"> 0.0590401 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 197 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3189966 </td>
   <td style="text-align:right;"> 0.0984319 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 198 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1428317 </td>
   <td style="text-align:right;"> 0.1537295 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 199 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3522619 </td>
   <td style="text-align:right;"> 0.0701244 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 200 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4937038 </td>
   <td style="text-align:right;"> 0.0091793 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 201 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0828490 </td>
   <td style="text-align:right;"> 0.0568506 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 202 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4350924 </td>
   <td style="text-align:right;"> 0.3668102 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 203 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5637960 </td>
   <td style="text-align:right;"> 0.0506983 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 204 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3005332 </td>
   <td style="text-align:right;"> 0.0367055 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 205 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2232321 </td>
   <td style="text-align:right;"> 0.0658237 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 206 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6257946 </td>
   <td style="text-align:right;"> 0.3373080 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 207 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1125551 </td>
   <td style="text-align:right;"> 0.0632472 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 208 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2774378 </td>
   <td style="text-align:right;"> 0.0814827 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 209 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4821408 </td>
   <td style="text-align:right;"> 0.0778421 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 210 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1076579 </td>
   <td style="text-align:right;"> 0.0956623 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 211 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3907574 </td>
   <td style="text-align:right;"> 0.0607522 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 212 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1203757 </td>
   <td style="text-align:right;"> 0.0708920 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 213 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2610952 </td>
   <td style="text-align:right;"> 0.1632016 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 214 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4931324 </td>
   <td style="text-align:right;"> 0.0156342 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 215 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1437807 </td>
   <td style="text-align:right;"> 0.0414703 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 216 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2139074 </td>
   <td style="text-align:right;"> 0.0267552 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 217 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1273957 </td>
   <td style="text-align:right;"> 0.0186172 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 218 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3592787 </td>
   <td style="text-align:right;"> 0.0517181 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 219 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.3562885 </td>
   <td style="text-align:right;"> 0.2386565 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 220 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7254731 </td>
   <td style="text-align:right;"> 0.2601762 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 221 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6637979 </td>
   <td style="text-align:right;"> 0.0582660 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 222 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5719600 </td>
   <td style="text-align:right;"> 0.0804353 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 223 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4642578 </td>
   <td style="text-align:right;"> 0.0675397 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 224 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2842014 </td>
   <td style="text-align:right;"> 0.0100923 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 225 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4109077 </td>
   <td style="text-align:right;"> 0.0424597 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 226 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3286377 </td>
   <td style="text-align:right;"> 0.2176010 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 227 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0494921 </td>
   <td style="text-align:right;"> 0.1492240 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 228 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5529329 </td>
   <td style="text-align:right;"> 0.1034737 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 229 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2200353 </td>
   <td style="text-align:right;"> 0.1829803 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 230 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6325457 </td>
   <td style="text-align:right;"> 0.2672998 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 231 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2466852 </td>
   <td style="text-align:right;"> 0.1812925 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 232 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2607934 </td>
   <td style="text-align:right;"> 0.0304099 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 233 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5462085 </td>
   <td style="text-align:right;"> 0.0298900 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 234 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1049839 </td>
   <td style="text-align:right;"> 0.1677156 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 235 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1860359 </td>
   <td style="text-align:right;"> 0.0082576 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 236 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6690087 </td>
   <td style="text-align:right;"> 0.0874200 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 237 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6319626 </td>
   <td style="text-align:right;"> 0.2243257 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 238 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9646117 </td>
   <td style="text-align:right;"> 0.1527869 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 239 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7175373 </td>
   <td style="text-align:right;"> 0.3428358 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 240 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5926664 </td>
   <td style="text-align:right;"> 0.2040500 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 241 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1822721 </td>
   <td style="text-align:right;"> 0.3053258 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 242 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4111723 </td>
   <td style="text-align:right;"> 0.0107488 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 243 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5460718 </td>
   <td style="text-align:right;"> 0.1468093 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 244 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0393239 </td>
   <td style="text-align:right;"> 0.0096748 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 245 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3441256 </td>
   <td style="text-align:right;"> 0.0992002 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 246 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4364391 </td>
   <td style="text-align:right;"> 0.0535544 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 247 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2748144 </td>
   <td style="text-align:right;"> 0.0305583 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 248 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7749291 </td>
   <td style="text-align:right;"> 0.2498915 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 249 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9412289 </td>
   <td style="text-align:right;"> 0.4249316 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 250 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6104680 </td>
   <td style="text-align:right;"> 0.0469561 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 251 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0674353 </td>
   <td style="text-align:right;"> 0.0310237 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 252 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5525887 </td>
   <td style="text-align:right;"> 0.4008905 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 253 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1564386 </td>
   <td style="text-align:right;"> 0.1304212 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 254 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0921223 </td>
   <td style="text-align:right;"> 0.0081703 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 255 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6192063 </td>
   <td style="text-align:right;"> 0.0569135 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 256 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5709531 </td>
   <td style="text-align:right;"> 0.0468653 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 257 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2392115 </td>
   <td style="text-align:right;"> 0.0639119 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 258 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4638430 </td>
   <td style="text-align:right;"> 0.1361828 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 259 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1422934 </td>
   <td style="text-align:right;"> 0.2143307 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 260 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4969819 </td>
   <td style="text-align:right;"> 0.2017904 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 261 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7137418 </td>
   <td style="text-align:right;"> 0.3162452 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 262 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8960371 </td>
   <td style="text-align:right;"> 0.0357972 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 263 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4571120 </td>
   <td style="text-align:right;"> 0.1084266 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 264 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8194382 </td>
   <td style="text-align:right;"> 0.0614808 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 265 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2791639 </td>
   <td style="text-align:right;"> 0.0265588 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 266 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2238215 </td>
   <td style="text-align:right;"> 0.1264698 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 267 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4009503 </td>
   <td style="text-align:right;"> 0.0342549 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 268 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1388433 </td>
   <td style="text-align:right;"> 0.0300056 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 269 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1246337 </td>
   <td style="text-align:right;"> 0.0789692 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 270 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6497995 </td>
   <td style="text-align:right;"> 0.3872448 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 271 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5018357 </td>
   <td style="text-align:right;"> 0.4489492 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 272 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5382585 </td>
   <td style="text-align:right;"> 0.0325571 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 273 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2670773 </td>
   <td style="text-align:right;"> 0.0565678 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 274 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3152211 </td>
   <td style="text-align:right;"> 0.1521353 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 275 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5927205 </td>
   <td style="text-align:right;"> 0.0845179 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 276 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3308402 </td>
   <td style="text-align:right;"> 0.0723066 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 277 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5654349 </td>
   <td style="text-align:right;"> 0.2876401 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 278 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1999635 </td>
   <td style="text-align:right;"> 0.0771409 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 279 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4445521 </td>
   <td style="text-align:right;"> 0.0678987 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 280 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0222674 </td>
   <td style="text-align:right;"> 0.0573056 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 281 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5564206 </td>
   <td style="text-align:right;"> 0.0409706 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 282 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0666726 </td>
   <td style="text-align:right;"> 0.0303731 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 283 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2901643 </td>
   <td style="text-align:right;"> 0.0491554 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 284 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2488059 </td>
   <td style="text-align:right;"> 0.0581107 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 285 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6130904 </td>
   <td style="text-align:right;"> 0.1043090 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 286 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3253941 </td>
   <td style="text-align:right;"> 0.0462973 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 287 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3067498 </td>
   <td style="text-align:right;"> 0.0333432 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 288 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4476785 </td>
   <td style="text-align:right;"> 0.1918746 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 289 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1467644 </td>
   <td style="text-align:right;"> 0.0009791 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 290 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2477774 </td>
   <td style="text-align:right;"> 0.2082405 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 291 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4438602 </td>
   <td style="text-align:right;"> 0.2088798 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 292 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0934995 </td>
   <td style="text-align:right;"> 0.0368292 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 293 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4321117 </td>
   <td style="text-align:right;"> 0.0651525 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 294 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8657016 </td>
   <td style="text-align:right;"> 0.0709558 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 295 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1797475 </td>
   <td style="text-align:right;"> 0.0271666 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 296 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9016632 </td>
   <td style="text-align:right;"> 0.2585079 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 297 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7307397 </td>
   <td style="text-align:right;"> 0.0305345 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 298 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0508427 </td>
   <td style="text-align:right;"> 0.0544824 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 299 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6154800 </td>
   <td style="text-align:right;"> 0.1498304 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 300 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1484258 </td>
   <td style="text-align:right;"> 0.2168997 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 301 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5988901 </td>
   <td style="text-align:right;"> 0.0048022 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 302 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2529359 </td>
   <td style="text-align:right;"> 0.0354284 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 303 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3800317 </td>
   <td style="text-align:right;"> 0.0387253 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 304 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4782104 </td>
   <td style="text-align:right;"> 0.2018345 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 305 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1717603 </td>
   <td style="text-align:right;"> 0.0066005 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 306 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2281118 </td>
   <td style="text-align:right;"> 0.2536653 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 307 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2091071 </td>
   <td style="text-align:right;"> 0.0935100 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 308 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3118771 </td>
   <td style="text-align:right;"> 0.0509130 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 309 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3908787 </td>
   <td style="text-align:right;"> 0.0010179 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 310 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2217837 </td>
   <td style="text-align:right;"> 0.0355324 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 311 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2393554 </td>
   <td style="text-align:right;"> 0.0043301 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 312 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2221083 </td>
   <td style="text-align:right;"> 0.0224704 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 313 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2897986 </td>
   <td style="text-align:right;"> 0.0357851 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 314 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3679980 </td>
   <td style="text-align:right;"> 0.0985389 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 315 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2063328 </td>
   <td style="text-align:right;"> 0.0241664 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 316 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7980705 </td>
   <td style="text-align:right;"> 0.5557752 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 317 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7011332 </td>
   <td style="text-align:right;"> 0.1217121 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 318 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2199078 </td>
   <td style="text-align:right;"> 0.0393279 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 319 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0374344 </td>
   <td style="text-align:right;"> 0.0735145 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 320 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7202453 </td>
   <td style="text-align:right;"> 0.3381126 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 321 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5870620 </td>
   <td style="text-align:right;"> 0.0666061 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 322 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1548464 </td>
   <td style="text-align:right;"> 0.0858643 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 323 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3264157 </td>
   <td style="text-align:right;"> 0.0741818 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 324 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5702607 </td>
   <td style="text-align:right;"> 0.1100356 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 325 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1551719 </td>
   <td style="text-align:right;"> 0.1280392 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 326 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2425765 </td>
   <td style="text-align:right;"> 0.0194494 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 327 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7799758 </td>
   <td style="text-align:right;"> 0.1822353 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 328 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3850676 </td>
   <td style="text-align:right;"> 0.2276844 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 329 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1119069 </td>
   <td style="text-align:right;"> 0.0352327 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 330 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4951180 </td>
   <td style="text-align:right;"> 0.5559196 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 331 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4701646 </td>
   <td style="text-align:right;"> 0.1619608 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 332 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3386734 </td>
   <td style="text-align:right;"> 0.0648201 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 333 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1792164 </td>
   <td style="text-align:right;"> 0.0316392 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 334 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7461309 </td>
   <td style="text-align:right;"> 0.2714034 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 335 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5429942 </td>
   <td style="text-align:right;"> 0.0440532 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 336 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1781737 </td>
   <td style="text-align:right;"> 0.0575498 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 337 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3106426 </td>
   <td style="text-align:right;"> 0.1556860 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 338 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2377923 </td>
   <td style="text-align:right;"> 0.2131017 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 339 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1129045 </td>
   <td style="text-align:right;"> 0.1154501 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 340 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4972346 </td>
   <td style="text-align:right;"> 0.3761177 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 341 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3381907 </td>
   <td style="text-align:right;"> 0.1022566 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 342 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1592998 </td>
   <td style="text-align:right;"> 0.0875539 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 343 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0930385 </td>
   <td style="text-align:right;"> 0.0824481 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 344 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3014464 </td>
   <td style="text-align:right;"> 0.2218246 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 345 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3400622 </td>
   <td style="text-align:right;"> 0.1277759 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 346 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3450766 </td>
   <td style="text-align:right;"> 0.0714901 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 347 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7502345 </td>
   <td style="text-align:right;"> 0.1604359 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 348 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2015859 </td>
   <td style="text-align:right;"> 0.0859530 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 349 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1933116 </td>
   <td style="text-align:right;"> 0.1091821 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 350 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3359925 </td>
   <td style="text-align:right;"> 0.0007922 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 351 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1885540 </td>
   <td style="text-align:right;"> 0.1028270 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 352 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8212002 </td>
   <td style="text-align:right;"> 0.0633288 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 353 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3221915 </td>
   <td style="text-align:right;"> 0.0436563 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 354 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1771635 </td>
   <td style="text-align:right;"> 0.1014514 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 355 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0489784 </td>
   <td style="text-align:right;"> 0.1975600 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 356 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5871185 </td>
   <td style="text-align:right;"> 0.2803930 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 357 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1855490 </td>
   <td style="text-align:right;"> 0.0201513 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 358 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1455502 </td>
   <td style="text-align:right;"> 0.3148218 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 359 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4359633 </td>
   <td style="text-align:right;"> 0.0764714 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 360 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6630928 </td>
   <td style="text-align:right;"> 0.3794182 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 361 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4617449 </td>
   <td style="text-align:right;"> 0.0264833 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 362 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2328375 </td>
   <td style="text-align:right;"> 0.0859652 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 363 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6625384 </td>
   <td style="text-align:right;"> 0.1353120 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 364 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1044106 </td>
   <td style="text-align:right;"> 0.2049119 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 365 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2759447 </td>
   <td style="text-align:right;"> 0.0223719 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 366 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1639856 </td>
   <td style="text-align:right;"> 0.0883773 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 367 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4431549 </td>
   <td style="text-align:right;"> 0.0000535 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 368 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3126993 </td>
   <td style="text-align:right;"> 0.0913046 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 369 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5605324 </td>
   <td style="text-align:right;"> 0.0001731 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 370 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.8182595 </td>
   <td style="text-align:right;"> 0.1101931 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 371 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3149744 </td>
   <td style="text-align:right;"> 0.0074307 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 372 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1896540 </td>
   <td style="text-align:right;"> 0.0046089 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 373 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8969756 </td>
   <td style="text-align:right;"> 0.0800963 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 374 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2355158 </td>
   <td style="text-align:right;"> 0.0574862 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 375 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2718637 </td>
   <td style="text-align:right;"> 0.1924012 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 376 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5801316 </td>
   <td style="text-align:right;"> 0.2472940 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 377 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1133573 </td>
   <td style="text-align:right;"> 0.1931672 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 378 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2103036 </td>
   <td style="text-align:right;"> 0.2156192 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 379 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4192938 </td>
   <td style="text-align:right;"> 0.0408267 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 380 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6235451 </td>
   <td style="text-align:right;"> 0.2211369 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 381 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1360486 </td>
   <td style="text-align:right;"> 0.0430455 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 382 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3120669 </td>
   <td style="text-align:right;"> 0.1428233 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 383 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2771298 </td>
   <td style="text-align:right;"> 0.1328359 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 384 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2267573 </td>
   <td style="text-align:right;"> 0.0953394 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 385 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2950944 </td>
   <td style="text-align:right;"> 0.0534758 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 386 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7331825 </td>
   <td style="text-align:right;"> 0.4202252 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 387 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0598610 </td>
   <td style="text-align:right;"> 0.0000285 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 388 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2271108 </td>
   <td style="text-align:right;"> 0.1358000 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 389 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4160992 </td>
   <td style="text-align:right;"> 0.1441568 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 390 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1914582 </td>
   <td style="text-align:right;"> 0.0016657 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 391 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7137085 </td>
   <td style="text-align:right;"> 0.2472323 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 392 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2814903 </td>
   <td style="text-align:right;"> 0.0065641 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 393 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1611738 </td>
   <td style="text-align:right;"> 0.0448978 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 394 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1251319 </td>
   <td style="text-align:right;"> 0.2437401 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 395 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2470422 </td>
   <td style="text-align:right;"> 0.0646942 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 396 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4838286 </td>
   <td style="text-align:right;"> 0.1569587 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 397 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2833124 </td>
   <td style="text-align:right;"> 0.0421309 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 398 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3731122 </td>
   <td style="text-align:right;"> 0.2743846 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 399 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2717042 </td>
   <td style="text-align:right;"> 0.0452610 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 400 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7815366 </td>
   <td style="text-align:right;"> 0.5779321 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 401 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9425677 </td>
   <td style="text-align:right;"> 0.1067537 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 402 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3359163 </td>
   <td style="text-align:right;"> 0.0577937 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 403 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7979672 </td>
   <td style="text-align:right;"> 0.2433580 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 404 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3614969 </td>
   <td style="text-align:right;"> 0.0483079 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 405 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3236445 </td>
   <td style="text-align:right;"> 0.0221224 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 406 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1856302 </td>
   <td style="text-align:right;"> 0.0510470 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 407 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2537576 </td>
   <td style="text-align:right;"> 0.0360568 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 408 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3672295 </td>
   <td style="text-align:right;"> 0.0342497 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 409 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0340531 </td>
   <td style="text-align:right;"> 0.0649519 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 410 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1792565 </td>
   <td style="text-align:right;"> 0.0835626 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 411 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4188983 </td>
   <td style="text-align:right;"> 0.0181398 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 412 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6369975 </td>
   <td style="text-align:right;"> 0.2020131 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 413 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1503794 </td>
   <td style="text-align:right;"> 0.0683492 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 414 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1740806 </td>
   <td style="text-align:right;"> 0.0867172 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 415 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3357280 </td>
   <td style="text-align:right;"> 0.0128647 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 416 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0612905 </td>
   <td style="text-align:right;"> 0.0104988 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 417 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4829044 </td>
   <td style="text-align:right;"> 0.2886935 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 418 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0290395 </td>
   <td style="text-align:right;"> 0.1022841 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 419 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1946353 </td>
   <td style="text-align:right;"> 0.0070581 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 420 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1522209 </td>
   <td style="text-align:right;"> 0.2362488 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 421 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0962778 </td>
   <td style="text-align:right;"> 0.2005386 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 422 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1151359 </td>
   <td style="text-align:right;"> 0.0798674 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 423 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3389233 </td>
   <td style="text-align:right;"> 0.1458367 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 424 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2621347 </td>
   <td style="text-align:right;"> 0.1149766 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 425 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7296896 </td>
   <td style="text-align:right;"> 0.6420904 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 426 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0885891 </td>
   <td style="text-align:right;"> 0.3170021 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 427 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2599283 </td>
   <td style="text-align:right;"> 0.0343877 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 428 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1399506 </td>
   <td style="text-align:right;"> 0.0031605 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 429 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1508967 </td>
   <td style="text-align:right;"> 0.0868588 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 430 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8875958 </td>
   <td style="text-align:right;"> 0.3930765 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 431 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4743532 </td>
   <td style="text-align:right;"> 0.3703327 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 432 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1191549 </td>
   <td style="text-align:right;"> 0.0630219 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 433 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2002430 </td>
   <td style="text-align:right;"> 0.0463646 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 434 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6978795 </td>
   <td style="text-align:right;"> 0.5093777 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 435 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1674615 </td>
   <td style="text-align:right;"> 0.1607621 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 436 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1289061 </td>
   <td style="text-align:right;"> 0.0190901 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 437 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2753661 </td>
   <td style="text-align:right;"> 0.0556928 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 438 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4589847 </td>
   <td style="text-align:right;"> 0.0334481 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 439 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3337529 </td>
   <td style="text-align:right;"> 0.0555125 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 440 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2469904 </td>
   <td style="text-align:right;"> 0.1125680 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 441 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3705508 </td>
   <td style="text-align:right;"> 0.2117135 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 442 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4730112 </td>
   <td style="text-align:right;"> 0.0020349 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 443 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2581750 </td>
   <td style="text-align:right;"> 0.0742372 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 444 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3867641 </td>
   <td style="text-align:right;"> 0.0224962 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 445 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5581414 </td>
   <td style="text-align:right;"> 0.1858400 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 446 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2379304 </td>
   <td style="text-align:right;"> 0.1020797 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 447 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2082369 </td>
   <td style="text-align:right;"> 0.1258148 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 448 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3268839 </td>
   <td style="text-align:right;"> 0.1120272 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 449 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3634058 </td>
   <td style="text-align:right;"> 0.1007799 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 450 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2613980 </td>
   <td style="text-align:right;"> 0.0352813 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 451 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1551418 </td>
   <td style="text-align:right;"> 0.0754075 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 452 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1332486 </td>
   <td style="text-align:right;"> 0.2380576 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 453 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3453193 </td>
   <td style="text-align:right;"> 0.0104153 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 454 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6314368 </td>
   <td style="text-align:right;"> 0.3384597 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 455 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1522274 </td>
   <td style="text-align:right;"> 0.0285654 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 456 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8803807 </td>
   <td style="text-align:right;"> 0.2305206 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 457 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7179034 </td>
   <td style="text-align:right;"> 0.2692874 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 458 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1865085 </td>
   <td style="text-align:right;"> 0.1068337 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 459 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3109043 </td>
   <td style="text-align:right;"> 0.0313327 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 460 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2761981 </td>
   <td style="text-align:right;"> 0.0466258 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 461 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6611553 </td>
   <td style="text-align:right;"> 0.4632382 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 462 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4831108 </td>
   <td style="text-align:right;"> 0.0364234 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 463 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4871380 </td>
   <td style="text-align:right;"> 0.0775412 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 464 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6058757 </td>
   <td style="text-align:right;"> 0.1160987 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 465 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1941506 </td>
   <td style="text-align:right;"> 0.0292513 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 466 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2009316 </td>
   <td style="text-align:right;"> 0.1058910 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 467 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3414201 </td>
   <td style="text-align:right;"> 0.0332621 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 468 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4300954 </td>
   <td style="text-align:right;"> 0.0360289 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 469 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2219794 </td>
   <td style="text-align:right;"> 0.1575472 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 470 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6530802 </td>
   <td style="text-align:right;"> 0.5262908 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 471 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1767082 </td>
   <td style="text-align:right;"> 0.2979416 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 472 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7460635 </td>
   <td style="text-align:right;"> 0.2262588 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 473 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2934948 </td>
   <td style="text-align:right;"> 0.0001390 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 474 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1172842 </td>
   <td style="text-align:right;"> 0.0065346 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 475 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3699870 </td>
   <td style="text-align:right;"> 0.2145771 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 476 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0392056 </td>
   <td style="text-align:right;"> 0.0560685 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 477 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5169853 </td>
   <td style="text-align:right;"> 0.1140903 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 478 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0591144 </td>
   <td style="text-align:right;"> 0.1280484 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 479 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0275551 </td>
   <td style="text-align:right;"> 0.1424414 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 480 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1555134 </td>
   <td style="text-align:right;"> 0.1034465 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 481 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3195816 </td>
   <td style="text-align:right;"> 0.0334764 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 482 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8698882 </td>
   <td style="text-align:right;"> 0.0809940 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 483 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1857793 </td>
   <td style="text-align:right;"> 0.0330226 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 484 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3578137 </td>
   <td style="text-align:right;"> 0.0839019 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 485 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6572982 </td>
   <td style="text-align:right;"> 0.2131185 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 486 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2686897 </td>
   <td style="text-align:right;"> 0.0138981 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 487 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3924957 </td>
   <td style="text-align:right;"> 0.0109869 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 488 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7320287 </td>
   <td style="text-align:right;"> 0.2070320 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 489 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3861259 </td>
   <td style="text-align:right;"> 0.0202252 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 490 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5760065 </td>
   <td style="text-align:right;"> 0.0927130 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 491 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7319096 </td>
   <td style="text-align:right;"> 0.1161725 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 492 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0987949 </td>
   <td style="text-align:right;"> 0.0865508 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 493 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2255842 </td>
   <td style="text-align:right;"> 0.1204460 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 494 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4513747 </td>
   <td style="text-align:right;"> 0.2875195 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 495 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2249622 </td>
   <td style="text-align:right;"> 0.0742227 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 496 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8039399 </td>
   <td style="text-align:right;"> 0.1070200 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 497 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1167886 </td>
   <td style="text-align:right;"> 0.0692747 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 498 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2335251 </td>
   <td style="text-align:right;"> 0.0150598 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 499 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3315752 </td>
   <td style="text-align:right;"> 0.1355804 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 500 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2185648 </td>
   <td style="text-align:right;"> 0.0638449 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 501 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3090506 </td>
   <td style="text-align:right;"> 0.0981766 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 502 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1688654 </td>
   <td style="text-align:right;"> 0.0857296 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 503 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3673843 </td>
   <td style="text-align:right;"> 0.0661663 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 504 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2696240 </td>
   <td style="text-align:right;"> 0.1585077 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 505 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2763063 </td>
   <td style="text-align:right;"> 0.1444402 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 506 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0402430 </td>
   <td style="text-align:right;"> 0.0336859 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 507 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1684352 </td>
   <td style="text-align:right;"> 0.0054439 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 508 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0732203 </td>
   <td style="text-align:right;"> 0.1104759 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 509 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4601862 </td>
   <td style="text-align:right;"> 0.2282235 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 510 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1961565 </td>
   <td style="text-align:right;"> 0.0136597 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 511 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2543371 </td>
   <td style="text-align:right;"> 0.1553210 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 512 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3464690 </td>
   <td style="text-align:right;"> 0.0305390 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 513 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6127573 </td>
   <td style="text-align:right;"> 0.5268572 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 514 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3840167 </td>
   <td style="text-align:right;"> 0.0221149 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 515 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5329308 </td>
   <td style="text-align:right;"> 0.0375160 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 516 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1909694 </td>
   <td style="text-align:right;"> 0.1962796 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 517 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2275389 </td>
   <td style="text-align:right;"> 0.0089870 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 518 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5535606 </td>
   <td style="text-align:right;"> 0.0766614 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 519 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2859582 </td>
   <td style="text-align:right;"> 0.0851062 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 520 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7968451 </td>
   <td style="text-align:right;"> 0.2343817 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 521 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1441314 </td>
   <td style="text-align:right;"> 0.1240820 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 522 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1778518 </td>
   <td style="text-align:right;"> 0.0535598 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 523 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3578689 </td>
   <td style="text-align:right;"> 0.0111177 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 524 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2885955 </td>
   <td style="text-align:right;"> 0.0422451 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 525 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1957578 </td>
   <td style="text-align:right;"> 0.0439383 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 526 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2200469 </td>
   <td style="text-align:right;"> 0.0214151 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 527 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5622723 </td>
   <td style="text-align:right;"> 0.1829615 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 528 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3299380 </td>
   <td style="text-align:right;"> 0.3698103 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 529 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8618178 </td>
   <td style="text-align:right;"> 0.3673786 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 530 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1340814 </td>
   <td style="text-align:right;"> 0.1778613 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 531 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7971357 </td>
   <td style="text-align:right;"> 0.3740360 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 532 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4495591 </td>
   <td style="text-align:right;"> 0.0599396 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 533 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2010623 </td>
   <td style="text-align:right;"> 0.0370442 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 534 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5844186 </td>
   <td style="text-align:right;"> 0.2558944 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 535 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4969992 </td>
   <td style="text-align:right;"> 0.2744800 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 536 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1706499 </td>
   <td style="text-align:right;"> 0.0379390 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 537 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4389616 </td>
   <td style="text-align:right;"> 0.1740866 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 538 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6172491 </td>
   <td style="text-align:right;"> 0.6165129 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 539 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1291410 </td>
   <td style="text-align:right;"> 0.0132532 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 540 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4283787 </td>
   <td style="text-align:right;"> 0.2299414 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 541 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4938005 </td>
   <td style="text-align:right;"> 0.4058184 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 542 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3709068 </td>
   <td style="text-align:right;"> 0.2220071 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 543 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8676253 </td>
   <td style="text-align:right;"> 0.4031051 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 544 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7533814 </td>
   <td style="text-align:right;"> 0.0865139 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 545 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4391471 </td>
   <td style="text-align:right;"> 0.0297972 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 546 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7664450 </td>
   <td style="text-align:right;"> 0.4435031 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 547 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4488832 </td>
   <td style="text-align:right;"> 0.0860575 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 548 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6970315 </td>
   <td style="text-align:right;"> 0.3454451 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 549 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9109829 </td>
   <td style="text-align:right;"> 0.3887570 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 550 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2490885 </td>
   <td style="text-align:right;"> 0.0086584 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 551 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5046840 </td>
   <td style="text-align:right;"> 0.0008714 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 552 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2429802 </td>
   <td style="text-align:right;"> 0.2286152 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 553 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0236840 </td>
   <td style="text-align:right;"> 0.1884366 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 554 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8649897 </td>
   <td style="text-align:right;"> 0.5597531 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 555 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3328414 </td>
   <td style="text-align:right;"> 0.0161834 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 556 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1804997 </td>
   <td style="text-align:right;"> 0.0000607 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 557 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3447449 </td>
   <td style="text-align:right;"> 0.0352764 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 558 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1288103 </td>
   <td style="text-align:right;"> 0.0739062 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 559 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1224487 </td>
   <td style="text-align:right;"> 0.1313370 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 560 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1535911 </td>
   <td style="text-align:right;"> 0.1206864 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 561 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5129190 </td>
   <td style="text-align:right;"> 0.0988038 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 562 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8087704 </td>
   <td style="text-align:right;"> 0.2476315 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 563 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5621703 </td>
   <td style="text-align:right;"> 0.1086114 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 564 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2075480 </td>
   <td style="text-align:right;"> 0.0785427 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 565 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4638527 </td>
   <td style="text-align:right;"> 0.1784115 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 566 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3299491 </td>
   <td style="text-align:right;"> 0.1474687 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 567 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1185291 </td>
   <td style="text-align:right;"> 0.0382266 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 568 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6101586 </td>
   <td style="text-align:right;"> 0.0608055 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 569 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2959310 </td>
   <td style="text-align:right;"> 0.0240841 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 570 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8783414 </td>
   <td style="text-align:right;"> 0.2103236 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 571 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2251644 </td>
   <td style="text-align:right;"> 0.0693526 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 572 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8451068 </td>
   <td style="text-align:right;"> 0.1859352 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 573 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0326999 </td>
   <td style="text-align:right;"> 0.2115205 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 574 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3794249 </td>
   <td style="text-align:right;"> 0.0484312 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 575 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7761780 </td>
   <td style="text-align:right;"> 0.1352634 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 576 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4096649 </td>
   <td style="text-align:right;"> 0.0146327 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 577 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0684273 </td>
   <td style="text-align:right;"> 0.0174831 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 578 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0957849 </td>
   <td style="text-align:right;"> 0.0570782 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 579 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2637568 </td>
   <td style="text-align:right;"> 0.4160230 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 580 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0801228 </td>
   <td style="text-align:right;"> 0.0076103 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 581 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4145006 </td>
   <td style="text-align:right;"> 0.4665844 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 582 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8125524 </td>
   <td style="text-align:right;"> 0.1151679 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 583 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6491093 </td>
   <td style="text-align:right;"> 0.3177922 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 584 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1208173 </td>
   <td style="text-align:right;"> 0.1062417 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 585 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8703159 </td>
   <td style="text-align:right;"> 0.2845327 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 586 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1087068 </td>
   <td style="text-align:right;"> 0.0615379 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 587 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3539526 </td>
   <td style="text-align:right;"> 0.1628341 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 588 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2797578 </td>
   <td style="text-align:right;"> 0.1746458 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 589 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6899688 </td>
   <td style="text-align:right;"> 0.3727213 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 590 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1540230 </td>
   <td style="text-align:right;"> 0.1836216 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 591 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1169925 </td>
   <td style="text-align:right;"> 0.0193658 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 592 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3820899 </td>
   <td style="text-align:right;"> 0.1310085 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 593 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8544356 </td>
   <td style="text-align:right;"> 0.4265337 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 594 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3678837 </td>
   <td style="text-align:right;"> 0.1656405 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 595 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1446232 </td>
   <td style="text-align:right;"> 0.0464258 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 596 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7274220 </td>
   <td style="text-align:right;"> 0.1294982 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 597 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4051222 </td>
   <td style="text-align:right;"> 0.0597255 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 598 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2512855 </td>
   <td style="text-align:right;"> 0.0045190 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 599 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9636131 </td>
   <td style="text-align:right;"> 0.1843317 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 600 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5385690 </td>
   <td style="text-align:right;"> 0.0410800 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 601 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1379219 </td>
   <td style="text-align:right;"> 0.0344974 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 602 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5703120 </td>
   <td style="text-align:right;"> 0.0558858 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 603 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2094265 </td>
   <td style="text-align:right;"> 0.0041960 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 604 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1626782 </td>
   <td style="text-align:right;"> 0.0048998 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 605 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2459555 </td>
   <td style="text-align:right;"> 0.1636632 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 606 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7340590 </td>
   <td style="text-align:right;"> 0.2094684 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 607 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2456843 </td>
   <td style="text-align:right;"> 0.0538345 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 608 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8167968 </td>
   <td style="text-align:right;"> 0.3900323 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 609 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2321862 </td>
   <td style="text-align:right;"> 0.0628720 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 610 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1938062 </td>
   <td style="text-align:right;"> 0.0770412 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 611 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3868030 </td>
   <td style="text-align:right;"> 0.1361429 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 612 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2527464 </td>
   <td style="text-align:right;"> 0.1746947 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 613 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4451225 </td>
   <td style="text-align:right;"> 0.0433161 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 614 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7230043 </td>
   <td style="text-align:right;"> 0.2590123 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 615 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4340854 </td>
   <td style="text-align:right;"> 0.1674380 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 616 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4367613 </td>
   <td style="text-align:right;"> 0.0942410 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 617 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4226915 </td>
   <td style="text-align:right;"> 0.3924435 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 618 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2865552 </td>
   <td style="text-align:right;"> 0.1560665 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 619 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7723195 </td>
   <td style="text-align:right;"> 0.6195900 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 620 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3860397 </td>
   <td style="text-align:right;"> 0.1654216 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 621 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7745692 </td>
   <td style="text-align:right;"> 0.4269230 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 622 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6816017 </td>
   <td style="text-align:right;"> 0.4526343 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 623 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2339010 </td>
   <td style="text-align:right;"> 0.1564381 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 624 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1721944 </td>
   <td style="text-align:right;"> 0.0337259 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 625 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3004707 </td>
   <td style="text-align:right;"> 0.1165080 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 626 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3295499 </td>
   <td style="text-align:right;"> 0.0483685 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 627 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2497413 </td>
   <td style="text-align:right;"> 0.1109695 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 628 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5725167 </td>
   <td style="text-align:right;"> 0.3529513 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 629 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3761180 </td>
   <td style="text-align:right;"> 0.0338357 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 630 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1537488 </td>
   <td style="text-align:right;"> 0.1365641 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 631 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5690736 </td>
   <td style="text-align:right;"> 0.0377012 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 632 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5698640 </td>
   <td style="text-align:right;"> 0.2202310 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 633 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0479312 </td>
   <td style="text-align:right;"> 0.1149653 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 634 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2967867 </td>
   <td style="text-align:right;"> 0.0699000 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 635 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4963919 </td>
   <td style="text-align:right;"> 0.0976156 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 636 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4687841 </td>
   <td style="text-align:right;"> 0.1237393 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 637 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6510899 </td>
   <td style="text-align:right;"> 0.3672775 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 638 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1110678 </td>
   <td style="text-align:right;"> 0.0140099 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 639 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7929139 </td>
   <td style="text-align:right;"> 0.1213625 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 640 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4290732 </td>
   <td style="text-align:right;"> 0.0810316 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 641 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4943856 </td>
   <td style="text-align:right;"> 0.0203818 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 642 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4790488 </td>
   <td style="text-align:right;"> 0.0158787 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 643 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5184161 </td>
   <td style="text-align:right;"> 0.4141488 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 644 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0897518 </td>
   <td style="text-align:right;"> 0.0424982 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 645 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0367157 </td>
   <td style="text-align:right;"> 0.1724306 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 646 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3987246 </td>
   <td style="text-align:right;"> 0.2651300 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 647 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4822107 </td>
   <td style="text-align:right;"> 0.1947973 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 648 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3584248 </td>
   <td style="text-align:right;"> 0.0173467 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 649 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1173414 </td>
   <td style="text-align:right;"> 0.0157160 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 650 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2167185 </td>
   <td style="text-align:right;"> 0.0994246 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 651 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7491887 </td>
   <td style="text-align:right;"> 0.0075216 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 652 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5100151 </td>
   <td style="text-align:right;"> 0.5685292 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 653 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3572131 </td>
   <td style="text-align:right;"> 0.0362222 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 654 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2728350 </td>
   <td style="text-align:right;"> 0.0434502 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 655 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1229233 </td>
   <td style="text-align:right;"> 0.0055107 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 656 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8566672 </td>
   <td style="text-align:right;"> 0.1424949 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 657 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7463164 </td>
   <td style="text-align:right;"> 0.5006201 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 658 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3461233 </td>
   <td style="text-align:right;"> 0.3231236 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 659 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2790522 </td>
   <td style="text-align:right;"> 0.0073351 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 660 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2511148 </td>
   <td style="text-align:right;"> 0.2086214 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 661 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7729313 </td>
   <td style="text-align:right;"> 0.0960994 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 662 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7920853 </td>
   <td style="text-align:right;"> 0.2355408 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 663 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1894453 </td>
   <td style="text-align:right;"> 0.0444489 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 664 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2952877 </td>
   <td style="text-align:right;"> 0.2177624 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 665 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2691231 </td>
   <td style="text-align:right;"> 0.0146870 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 666 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1587101 </td>
   <td style="text-align:right;"> 0.0677312 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 667 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.3491965 </td>
   <td style="text-align:right;"> 0.5802743 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 668 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1141027 </td>
   <td style="text-align:right;"> 0.0774941 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 669 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1185058 </td>
   <td style="text-align:right;"> 0.0963584 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 670 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0419772 </td>
   <td style="text-align:right;"> 0.0958156 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 671 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5244293 </td>
   <td style="text-align:right;"> 0.1351808 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 672 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3118381 </td>
   <td style="text-align:right;"> 0.0136601 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 673 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1106542 </td>
   <td style="text-align:right;"> 0.2044908 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 674 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4286929 </td>
   <td style="text-align:right;"> 0.0064157 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 675 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4592984 </td>
   <td style="text-align:right;"> 0.0777560 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 676 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2422755 </td>
   <td style="text-align:right;"> 0.0619158 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 677 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6185700 </td>
   <td style="text-align:right;"> 0.1725664 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 678 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2663205 </td>
   <td style="text-align:right;"> 0.0608686 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 679 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3745372 </td>
   <td style="text-align:right;"> 0.0345080 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 680 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4746188 </td>
   <td style="text-align:right;"> 0.0305533 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 681 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1937168 </td>
   <td style="text-align:right;"> 0.0092319 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 682 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1225569 </td>
   <td style="text-align:right;"> 0.1140539 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 683 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7378492 </td>
   <td style="text-align:right;"> 0.2417544 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 684 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6991036 </td>
   <td style="text-align:right;"> 0.2695197 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 685 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5409935 </td>
   <td style="text-align:right;"> 0.1598990 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 686 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1986393 </td>
   <td style="text-align:right;"> 0.0335340 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 687 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1630779 </td>
   <td style="text-align:right;"> 0.1953841 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 688 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2449417 </td>
   <td style="text-align:right;"> 0.1474460 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 689 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7121075 </td>
   <td style="text-align:right;"> 0.0655642 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 690 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3506171 </td>
   <td style="text-align:right;"> 0.0210876 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 691 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3944155 </td>
   <td style="text-align:right;"> 0.1481200 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 692 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4681206 </td>
   <td style="text-align:right;"> 0.0706887 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 693 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0788069 </td>
   <td style="text-align:right;"> 0.0896277 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 694 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1203911 </td>
   <td style="text-align:right;"> 0.0947510 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 695 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0648646 </td>
   <td style="text-align:right;"> 0.1147799 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 696 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0089148 </td>
   <td style="text-align:right;"> 0.2759649 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 697 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1961822 </td>
   <td style="text-align:right;"> 0.1511826 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 698 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3722375 </td>
   <td style="text-align:right;"> 0.0177244 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 699 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1932750 </td>
   <td style="text-align:right;"> 0.2001716 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 700 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2592303 </td>
   <td style="text-align:right;"> 0.0953189 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 701 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4862735 </td>
   <td style="text-align:right;"> 0.2097730 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 702 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3335374 </td>
   <td style="text-align:right;"> 0.1192295 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 703 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1540094 </td>
   <td style="text-align:right;"> 0.0259085 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 704 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8022977 </td>
   <td style="text-align:right;"> 0.3639793 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 705 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4087870 </td>
   <td style="text-align:right;"> 0.0724240 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 706 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2309709 </td>
   <td style="text-align:right;"> 0.1559693 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 707 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0990365 </td>
   <td style="text-align:right;"> 0.2226230 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 708 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4309276 </td>
   <td style="text-align:right;"> 0.0444818 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 709 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6517186 </td>
   <td style="text-align:right;"> 0.0140537 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 710 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4943045 </td>
   <td style="text-align:right;"> 0.2871065 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 711 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1978942 </td>
   <td style="text-align:right;"> 0.0737145 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 712 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1901711 </td>
   <td style="text-align:right;"> 0.0062110 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 713 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1813782 </td>
   <td style="text-align:right;"> 0.0498777 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 714 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2096770 </td>
   <td style="text-align:right;"> 0.0430597 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 715 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4505667 </td>
   <td style="text-align:right;"> 0.2537298 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 716 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3403383 </td>
   <td style="text-align:right;"> 0.0908296 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 717 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0457916 </td>
   <td style="text-align:right;"> 0.1052418 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 718 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2811248 </td>
   <td style="text-align:right;"> 0.1118001 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 719 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6441177 </td>
   <td style="text-align:right;"> 0.1491832 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 720 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0233246 </td>
   <td style="text-align:right;"> 0.0028043 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 721 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1482002 </td>
   <td style="text-align:right;"> 0.0678495 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 722 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2913134 </td>
   <td style="text-align:right;"> 0.0140580 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 723 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6615097 </td>
   <td style="text-align:right;"> 0.0153822 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 724 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7748789 </td>
   <td style="text-align:right;"> 0.3114189 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 725 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0955659 </td>
   <td style="text-align:right;"> 0.0085394 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 726 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1148560 </td>
   <td style="text-align:right;"> 0.0755206 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 727 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6206792 </td>
   <td style="text-align:right;"> 0.5148634 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 728 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3572678 </td>
   <td style="text-align:right;"> 0.1101034 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 729 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2252816 </td>
   <td style="text-align:right;"> 0.0564419 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 730 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0630456 </td>
   <td style="text-align:right;"> 0.0546804 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 731 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1748537 </td>
   <td style="text-align:right;"> 0.0193700 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 732 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7143634 </td>
   <td style="text-align:right;"> 0.2831869 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 733 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2465402 </td>
   <td style="text-align:right;"> 0.0259759 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 734 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8053946 </td>
   <td style="text-align:right;"> 0.0525891 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 735 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3013673 </td>
   <td style="text-align:right;"> 0.0262300 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 736 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1638034 </td>
   <td style="text-align:right;"> 0.0660205 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 737 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8013582 </td>
   <td style="text-align:right;"> 0.1211881 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 738 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6173471 </td>
   <td style="text-align:right;"> 0.2290614 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 739 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1183476 </td>
   <td style="text-align:right;"> 0.1156137 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 740 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3047775 </td>
   <td style="text-align:right;"> 0.0245975 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 741 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.3949379 </td>
   <td style="text-align:right;"> 0.3120724 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 742 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2724633 </td>
   <td style="text-align:right;"> 0.0691951 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 743 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4387954 </td>
   <td style="text-align:right;"> 0.0739108 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 744 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2376880 </td>
   <td style="text-align:right;"> 0.0716190 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 745 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1051168 </td>
   <td style="text-align:right;"> 0.1814030 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 746 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1197661 </td>
   <td style="text-align:right;"> 0.0117424 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 747 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1525249 </td>
   <td style="text-align:right;"> 0.0311800 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 748 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5906275 </td>
   <td style="text-align:right;"> 0.0605024 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 749 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2490620 </td>
   <td style="text-align:right;"> 0.0044771 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 750 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8406727 </td>
   <td style="text-align:right;"> 0.1236260 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 751 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6280848 </td>
   <td style="text-align:right;"> 0.0219475 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 752 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1653810 </td>
   <td style="text-align:right;"> 0.0081485 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 753 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2041446 </td>
   <td style="text-align:right;"> 0.1213788 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 754 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3606086 </td>
   <td style="text-align:right;"> 0.1284986 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 755 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2847369 </td>
   <td style="text-align:right;"> 0.0640068 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 756 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3749346 </td>
   <td style="text-align:right;"> 0.0829414 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 757 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2736738 </td>
   <td style="text-align:right;"> 0.0317129 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 758 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7545655 </td>
   <td style="text-align:right;"> 0.8392892 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 759 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3939484 </td>
   <td style="text-align:right;"> 0.1306077 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 760 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2758522 </td>
   <td style="text-align:right;"> 0.0725549 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 761 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4295034 </td>
   <td style="text-align:right;"> 0.1045815 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 762 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2426049 </td>
   <td style="text-align:right;"> 0.1384155 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 763 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3838058 </td>
   <td style="text-align:right;"> 0.0452202 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 764 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0669519 </td>
   <td style="text-align:right;"> 0.0625854 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 765 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2885307 </td>
   <td style="text-align:right;"> 0.0220127 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 766 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1925752 </td>
   <td style="text-align:right;"> 0.0228189 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 767 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1024535 </td>
   <td style="text-align:right;"> 0.2205381 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 768 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2094470 </td>
   <td style="text-align:right;"> 0.0559626 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 769 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3668336 </td>
   <td style="text-align:right;"> 0.0470419 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 770 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3047314 </td>
   <td style="text-align:right;"> 0.1466996 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 771 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7150083 </td>
   <td style="text-align:right;"> 0.1947152 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 772 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9273173 </td>
   <td style="text-align:right;"> 0.4301916 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 773 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4823060 </td>
   <td style="text-align:right;"> 0.1097429 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 774 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6245620 </td>
   <td style="text-align:right;"> 0.2709078 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 775 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0882106 </td>
   <td style="text-align:right;"> 0.1753987 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 776 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2324162 </td>
   <td style="text-align:right;"> 0.0751665 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 777 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5776425 </td>
   <td style="text-align:right;"> 0.0076786 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 778 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2618083 </td>
   <td style="text-align:right;"> 0.2330893 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 779 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0611008 </td>
   <td style="text-align:right;"> 0.1157483 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 780 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.3834008 </td>
   <td style="text-align:right;"> 0.5587065 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 781 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3460657 </td>
   <td style="text-align:right;"> 0.0122958 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 782 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6113043 </td>
   <td style="text-align:right;"> 0.2050585 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 783 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3220235 </td>
   <td style="text-align:right;"> 0.1860059 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 784 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6350442 </td>
   <td style="text-align:right;"> 0.0265801 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 785 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9109223 </td>
   <td style="text-align:right;"> 0.1912240 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 786 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2878731 </td>
   <td style="text-align:right;"> 0.0142476 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 787 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0763632 </td>
   <td style="text-align:right;"> 0.0096445 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 788 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1605866 </td>
   <td style="text-align:right;"> 0.0521916 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 789 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2416386 </td>
   <td style="text-align:right;"> 0.0635546 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 790 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8130609 </td>
   <td style="text-align:right;"> 0.3012782 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 791 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8967044 </td>
   <td style="text-align:right;"> 0.1398970 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 792 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.8333232 </td>
   <td style="text-align:right;"> 0.1715959 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 793 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3094314 </td>
   <td style="text-align:right;"> 0.0020901 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 794 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1804158 </td>
   <td style="text-align:right;"> 0.1709436 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 795 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6164485 </td>
   <td style="text-align:right;"> 0.5079442 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 796 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1126226 </td>
   <td style="text-align:right;"> 0.0251864 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 797 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4551277 </td>
   <td style="text-align:right;"> 0.1314303 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 798 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2451396 </td>
   <td style="text-align:right;"> 0.0506947 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 799 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6585117 </td>
   <td style="text-align:right;"> 0.1205503 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 800 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4330338 </td>
   <td style="text-align:right;"> 0.0054705 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 801 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1676798 </td>
   <td style="text-align:right;"> 0.1090626 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 802 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4159585 </td>
   <td style="text-align:right;"> 0.0111157 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 803 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1639314 </td>
   <td style="text-align:right;"> 0.0698212 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 804 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1897540 </td>
   <td style="text-align:right;"> 0.1816467 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 805 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4677916 </td>
   <td style="text-align:right;"> 0.0146899 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 806 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.3909375 </td>
   <td style="text-align:right;"> 0.4346251 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 807 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2808062 </td>
   <td style="text-align:right;"> 0.0551947 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 808 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1008304 </td>
   <td style="text-align:right;"> 0.0379273 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 809 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4261159 </td>
   <td style="text-align:right;"> 0.0673499 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 810 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3786363 </td>
   <td style="text-align:right;"> 0.1704106 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 811 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1957474 </td>
   <td style="text-align:right;"> 0.1478642 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 812 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3953025 </td>
   <td style="text-align:right;"> 0.2103177 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 813 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1948532 </td>
   <td style="text-align:right;"> 0.0364429 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 814 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5479496 </td>
   <td style="text-align:right;"> 0.2582130 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 815 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1665344 </td>
   <td style="text-align:right;"> 0.0564988 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 816 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4715350 </td>
   <td style="text-align:right;"> 0.0021130 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 817 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4459142 </td>
   <td style="text-align:right;"> 0.3007814 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 818 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5986866 </td>
   <td style="text-align:right;"> 0.2039931 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 819 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1724715 </td>
   <td style="text-align:right;"> 0.2080799 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 820 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5201056 </td>
   <td style="text-align:right;"> 0.1189367 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 821 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0787927 </td>
   <td style="text-align:right;"> 0.0758708 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 822 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2020783 </td>
   <td style="text-align:right;"> 0.0237104 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 823 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1590696 </td>
   <td style="text-align:right;"> 0.0928338 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 824 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5236976 </td>
   <td style="text-align:right;"> 0.3321895 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 825 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1370198 </td>
   <td style="text-align:right;"> 0.0787671 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 826 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2166835 </td>
   <td style="text-align:right;"> 0.0886149 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 827 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2775457 </td>
   <td style="text-align:right;"> 0.1608884 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 828 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1776114 </td>
   <td style="text-align:right;"> 0.0040673 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 829 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0404112 </td>
   <td style="text-align:right;"> 0.0102956 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 830 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3373643 </td>
   <td style="text-align:right;"> 0.0482075 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 831 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3913888 </td>
   <td style="text-align:right;"> 0.1077750 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 832 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3141312 </td>
   <td style="text-align:right;"> 0.0378464 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 833 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1969856 </td>
   <td style="text-align:right;"> 0.2672659 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 834 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5018550 </td>
   <td style="text-align:right;"> 0.0614171 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 835 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5513963 </td>
   <td style="text-align:right;"> 0.0711893 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 836 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0209251 </td>
   <td style="text-align:right;"> 0.0029712 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 837 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5647660 </td>
   <td style="text-align:right;"> 0.0909543 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 838 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0508066 </td>
   <td style="text-align:right;"> 0.0776953 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 839 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2211255 </td>
   <td style="text-align:right;"> 0.0919704 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 840 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1115221 </td>
   <td style="text-align:right;"> 0.0739804 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 841 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5295253 </td>
   <td style="text-align:right;"> 0.3390442 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 842 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6199439 </td>
   <td style="text-align:right;"> 0.0992515 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 843 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4060238 </td>
   <td style="text-align:right;"> 0.0193230 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 844 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3960205 </td>
   <td style="text-align:right;"> 0.0602339 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 845 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0333371 </td>
   <td style="text-align:right;"> 0.0027346 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 846 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3270285 </td>
   <td style="text-align:right;"> 0.1455846 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 847 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9709373 </td>
   <td style="text-align:right;"> 0.2456967 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 848 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4911176 </td>
   <td style="text-align:right;"> 0.1445456 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 849 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1277584 </td>
   <td style="text-align:right;"> 0.0593151 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 850 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5121528 </td>
   <td style="text-align:right;"> 0.0450260 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 851 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0817631 </td>
   <td style="text-align:right;"> 0.0734781 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 852 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7384763 </td>
   <td style="text-align:right;"> 0.0364527 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 853 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5881034 </td>
   <td style="text-align:right;"> 0.5803552 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 854 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4652999 </td>
   <td style="text-align:right;"> 0.1278170 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 855 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3542932 </td>
   <td style="text-align:right;"> 0.0172898 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 856 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1168135 </td>
   <td style="text-align:right;"> 0.0549241 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 857 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9622067 </td>
   <td style="text-align:right;"> 0.2097417 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 858 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2925032 </td>
   <td style="text-align:right;"> 0.0244553 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 859 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3318371 </td>
   <td style="text-align:right;"> 0.0358698 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 860 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5842017 </td>
   <td style="text-align:right;"> 0.3147208 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 861 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2901133 </td>
   <td style="text-align:right;"> 0.1150660 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 862 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5621037 </td>
   <td style="text-align:right;"> 0.0351408 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 863 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4042342 </td>
   <td style="text-align:right;"> 0.1723537 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 864 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3683758 </td>
   <td style="text-align:right;"> 0.1098961 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 865 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4864739 </td>
   <td style="text-align:right;"> 0.1037695 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 866 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1762887 </td>
   <td style="text-align:right;"> 0.0552744 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 867 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3229637 </td>
   <td style="text-align:right;"> 0.0382123 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 868 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1825374 </td>
   <td style="text-align:right;"> 0.0992969 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 869 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5041741 </td>
   <td style="text-align:right;"> 0.0037634 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 870 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1739317 </td>
   <td style="text-align:right;"> 0.1169451 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 871 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4720615 </td>
   <td style="text-align:right;"> 0.0376770 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 872 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2829537 </td>
   <td style="text-align:right;"> 0.0405641 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 873 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5881154 </td>
   <td style="text-align:right;"> 0.0268618 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 874 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2689348 </td>
   <td style="text-align:right;"> 0.0485935 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 875 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6783517 </td>
   <td style="text-align:right;"> 0.3960069 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 876 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4044584 </td>
   <td style="text-align:right;"> 0.0386217 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 877 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3789005 </td>
   <td style="text-align:right;"> 0.0624835 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 878 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1799843 </td>
   <td style="text-align:right;"> 0.0634328 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 879 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8714664 </td>
   <td style="text-align:right;"> 0.2692599 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 880 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0577515 </td>
   <td style="text-align:right;"> 0.0274066 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 881 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2022732 </td>
   <td style="text-align:right;"> 0.0920394 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 882 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.9427614 </td>
   <td style="text-align:right;"> 0.0725508 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 883 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2398557 </td>
   <td style="text-align:right;"> 0.0100365 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 884 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1010700 </td>
   <td style="text-align:right;"> 0.0841546 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 885 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4486899 </td>
   <td style="text-align:right;"> 0.1546897 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 886 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7365379 </td>
   <td style="text-align:right;"> 0.3507346 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 887 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1777542 </td>
   <td style="text-align:right;"> 0.0609476 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 888 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2096395 </td>
   <td style="text-align:right;"> 0.0509506 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 889 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0775714 </td>
   <td style="text-align:right;"> 0.0693333 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 890 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4587942 </td>
   <td style="text-align:right;"> 0.0096431 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 891 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7070970 </td>
   <td style="text-align:right;"> 0.1005526 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 892 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1344308 </td>
   <td style="text-align:right;"> 0.0449222 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 893 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1011941 </td>
   <td style="text-align:right;"> 0.0722110 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 894 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0709064 </td>
   <td style="text-align:right;"> 0.1081679 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 895 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4789908 </td>
   <td style="text-align:right;"> 0.1191407 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 896 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0553205 </td>
   <td style="text-align:right;"> 0.2604779 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 897 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3628469 </td>
   <td style="text-align:right;"> 0.0650302 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 898 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3074337 </td>
   <td style="text-align:right;"> 0.2726579 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 899 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0178357 </td>
   <td style="text-align:right;"> 0.0777752 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 900 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2773351 </td>
   <td style="text-align:right;"> 0.0490673 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 901 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5002400 </td>
   <td style="text-align:right;"> 0.4449891 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 902 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1387347 </td>
   <td style="text-align:right;"> 0.0752559 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 903 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4453205 </td>
   <td style="text-align:right;"> 0.2817423 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 904 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4883823 </td>
   <td style="text-align:right;"> 0.1764105 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 905 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7353278 </td>
   <td style="text-align:right;"> 0.1062779 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 906 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0133592 </td>
   <td style="text-align:right;"> 0.2705818 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 907 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4596232 </td>
   <td style="text-align:right;"> 0.0209632 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 908 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5706745 </td>
   <td style="text-align:right;"> 0.5167827 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 909 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6345422 </td>
   <td style="text-align:right;"> 0.0713240 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 910 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3607425 </td>
   <td style="text-align:right;"> 0.1147224 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 911 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0738218 </td>
   <td style="text-align:right;"> 0.0543018 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 912 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3961998 </td>
   <td style="text-align:right;"> 0.1811612 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 913 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7600008 </td>
   <td style="text-align:right;"> 0.2046104 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 914 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5430042 </td>
   <td style="text-align:right;"> 0.0781537 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 915 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2412892 </td>
   <td style="text-align:right;"> 0.0114035 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 916 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7702111 </td>
   <td style="text-align:right;"> 0.1730646 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 917 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2041400 </td>
   <td style="text-align:right;"> 0.1788210 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 918 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2067463 </td>
   <td style="text-align:right;"> 0.0027614 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 919 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2908678 </td>
   <td style="text-align:right;"> 0.0825326 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 920 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1161490 </td>
   <td style="text-align:right;"> 0.0093133 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 921 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7788962 </td>
   <td style="text-align:right;"> 0.3642520 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 922 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5606166 </td>
   <td style="text-align:right;"> 0.0986870 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 923 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5618264 </td>
   <td style="text-align:right;"> 0.0778901 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 924 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8191342 </td>
   <td style="text-align:right;"> 0.2220173 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 925 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3544237 </td>
   <td style="text-align:right;"> 0.1705480 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 926 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3060233 </td>
   <td style="text-align:right;"> 0.0031623 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 927 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0951945 </td>
   <td style="text-align:right;"> 0.1561761 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 928 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3405651 </td>
   <td style="text-align:right;"> 0.0907588 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 929 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1471333 </td>
   <td style="text-align:right;"> 0.0099950 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 930 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1171644 </td>
   <td style="text-align:right;"> 0.0209123 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 931 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.2553160 </td>
   <td style="text-align:right;"> 0.2088026 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 932 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1634369 </td>
   <td style="text-align:right;"> 0.0598434 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 933 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2575037 </td>
   <td style="text-align:right;"> 0.1120798 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 934 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1277001 </td>
   <td style="text-align:right;"> 0.0425276 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 935 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6231792 </td>
   <td style="text-align:right;"> 0.4404279 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 936 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3956411 </td>
   <td style="text-align:right;"> 0.1075709 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 937 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3981387 </td>
   <td style="text-align:right;"> 0.0200188 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 938 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6684402 </td>
   <td style="text-align:right;"> 0.7447481 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 939 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5441582 </td>
   <td style="text-align:right;"> 0.1712525 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 940 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.6703875 </td>
   <td style="text-align:right;"> 0.1464680 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 941 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6545359 </td>
   <td style="text-align:right;"> 0.1426403 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 942 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3185889 </td>
   <td style="text-align:right;"> 0.0449455 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 943 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3015922 </td>
   <td style="text-align:right;"> 0.0205052 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 944 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3405960 </td>
   <td style="text-align:right;"> 0.0095643 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 945 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3678717 </td>
   <td style="text-align:right;"> 0.0209196 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 946 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3141545 </td>
   <td style="text-align:right;"> 0.2061634 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 947 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4361889 </td>
   <td style="text-align:right;"> 0.0153102 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 948 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2226497 </td>
   <td style="text-align:right;"> 0.0976929 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 949 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5661258 </td>
   <td style="text-align:right;"> 0.0163826 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 950 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2781642 </td>
   <td style="text-align:right;"> 0.1331159 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 951 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0524405 </td>
   <td style="text-align:right;"> 0.0181489 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 952 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2659978 </td>
   <td style="text-align:right;"> 0.0732174 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 953 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.4943057 </td>
   <td style="text-align:right;"> 0.3306243 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 954 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2980307 </td>
   <td style="text-align:right;"> 0.0055951 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 955 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0407442 </td>
   <td style="text-align:right;"> 0.0711394 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 956 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8817052 </td>
   <td style="text-align:right;"> 0.2807571 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 957 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1015158 </td>
   <td style="text-align:right;"> 0.0885222 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 958 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1274028 </td>
   <td style="text-align:right;"> 0.1172073 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 959 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1213396 </td>
   <td style="text-align:right;"> 0.1105127 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 960 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1505583 </td>
   <td style="text-align:right;"> 0.1084225 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 961 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.5683462 </td>
   <td style="text-align:right;"> 0.0908353 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 962 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1461535 </td>
   <td style="text-align:right;"> 0.0753300 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 963 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2051153 </td>
   <td style="text-align:right;"> 0.0490010 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 964 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3243743 </td>
   <td style="text-align:right;"> 0.0861758 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 965 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.7601498 </td>
   <td style="text-align:right;"> 0.5954401 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 966 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1468715 </td>
   <td style="text-align:right;"> 0.0785976 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 967 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1921927 </td>
   <td style="text-align:right;"> 0.0023311 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 968 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1045084 </td>
   <td style="text-align:right;"> 0.1506448 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 969 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0284605 </td>
   <td style="text-align:right;"> 0.0537722 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 970 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1907502 </td>
   <td style="text-align:right;"> 0.0468375 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 971 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0775298 </td>
   <td style="text-align:right;"> 0.0450016 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 972 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0397872 </td>
   <td style="text-align:right;"> 0.0455964 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 973 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.6738369 </td>
   <td style="text-align:right;"> 0.1457493 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 974 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.7101354 </td>
   <td style="text-align:right;"> 0.0488589 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 975 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1852351 </td>
   <td style="text-align:right;"> 0.0526056 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 976 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1650283 </td>
   <td style="text-align:right;"> 0.1296263 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 977 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8527480 </td>
   <td style="text-align:right;"> 0.3100229 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 978 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.4508088 </td>
   <td style="text-align:right;"> 0.0683253 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 979 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0151627 </td>
   <td style="text-align:right;"> 0.0975475 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 980 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3383920 </td>
   <td style="text-align:right;"> 0.0198834 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 981 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2107117 </td>
   <td style="text-align:right;"> 0.2183028 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 982 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1582815 </td>
   <td style="text-align:right;"> 0.1085090 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 983 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.8412575 </td>
   <td style="text-align:right;"> 0.4199985 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 984 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2459407 </td>
   <td style="text-align:right;"> 0.0567238 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 985 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.2533682 </td>
   <td style="text-align:right;"> 0.2898681 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 986 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2826326 </td>
   <td style="text-align:right;"> 0.1708397 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 987 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1377412 </td>
   <td style="text-align:right;"> 0.2415585 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 988 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2951616 </td>
   <td style="text-align:right;"> 0.1323967 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 989 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3880202 </td>
   <td style="text-align:right;"> 0.0116131 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 990 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1945712 </td>
   <td style="text-align:right;"> 0.0840691 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 991 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1217294 </td>
   <td style="text-align:right;"> 0.0064640 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 992 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1776990 </td>
   <td style="text-align:right;"> 0.2098731 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 993 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1693604 </td>
   <td style="text-align:right;"> 0.0376889 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 994 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.0729042 </td>
   <td style="text-align:right;"> 0.0757715 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 995 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1531317 </td>
   <td style="text-align:right;"> 0.0529123 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 996 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 0.5631179 </td>
   <td style="text-align:right;"> 0.3195622 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 997 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.2431798 </td>
   <td style="text-align:right;"> 0.0271777 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 998 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3569686 </td>
   <td style="text-align:right;"> 0.0919339 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 999 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.3579213 </td>
   <td style="text-align:right;"> 0.0195705 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 1000 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 0.1722501 </td>
   <td style="text-align:right;"> 0.0433818 </td>
  </tr>
</tbody>
</table></div>

`````
:::
:::





::: {.cell}

```{.r .cell-code}
# 4. Função para calcular métricas em massa (Vários Thresholds)
calcular_curva <- function(probs, real, nome_modelo) {
  thresholds <- seq(0.05, 0.95, by = 0.01)
  
  map_df(thresholds, function(t) {
    preds <- ifelse(probs >= t, 1, 0)
    tp <- sum(preds == 1 & real == 1)
    fp <- sum(preds == 1 & real == 0)
    fn <- sum(preds == 0 & real == 1)
    
    precisao <- ifelse((tp + fp) == 0, 1, tp / (tp + fp))
    recall <- tp / (tp + fn)
    
    data.frame(Modelo = nome_modelo, Threshold = t, Precisao = precisao, Recall = recall)
  })
}

# 5. Gerando os dados para o gráfico
library(purrr) # para o map_df
tradeoff_A <- calcular_curva(aula_data$prob_mod_A, aula_data$real, "Modelo A")
tradeoff_B <- calcular_curva(aula_data$prob_mod_B, aula_data$real, "Modelo B")

df_plot <- bind_rows(tradeoff_A, tradeoff_B)
```
:::



::: {.cell}

```{.r .cell-code}
df_plot |> 
  # pivot_longer(Precisao:Recall, names_to = "Metrica", values_to = "Valor") |> 
  pivot_wider(names_from = Modelo, values_from = Precisao:Recall, names_sep = " ") |> 
  knitr::kable()
```

::: {.cell-output-display}


| Threshold| Precisao Modelo A| Precisao Modelo B| Recall Modelo A| Recall Modelo B|
|---------:|-----------------:|-----------------:|---------------:|---------------:|
|      0.05|         0.2043344|         0.2842566|       1.0000000|       0.9848485|
|      0.06|         0.2062500|         0.3063492|       1.0000000|       0.9747475|
|      0.07|         0.2082019|         0.3264249|       1.0000000|       0.9545455|
|      0.08|         0.2101911|         0.3542857|       1.0000000|       0.9393939|
|      0.09|         0.2119914|         0.3788820|       1.0000000|       0.9242424|
|      0.10|         0.2154516|         0.4027149|       1.0000000|       0.8989899|
|      0.11|         0.2185430|         0.4278729|       1.0000000|       0.8838384|
|      0.12|         0.2260274|         0.4621622|       1.0000000|       0.8636364|
|      0.13|         0.2313084|         0.4770115|       1.0000000|       0.8383838|
|      0.14|         0.2348754|         0.4969512|       1.0000000|       0.8232323|
|      0.15|         0.2394196|         0.5247525|       1.0000000|       0.8030303|
|      0.16|         0.2456576|         0.5508772|       1.0000000|       0.7929293|
|      0.17|         0.2515883|         0.5677656|       1.0000000|       0.7828283|
|      0.18|         0.2588235|         0.5952381|       1.0000000|       0.7575758|
|      0.19|         0.2661290|         0.6170213|       1.0000000|       0.7323232|
|      0.20|         0.2757660|         0.6441441|       1.0000000|       0.7222222|
|      0.21|         0.2840746|         0.6769231|       1.0000000|       0.6666667|
|      0.22|         0.2890511|         0.7111111|       1.0000000|       0.6464646|
|      0.23|         0.2986425|         0.7378049|       1.0000000|       0.6111111|
|      0.24|         0.3060278|         0.7581699|       1.0000000|       0.5858586|
|      0.25|         0.3173077|         0.7535211|       1.0000000|       0.5404040|
|      0.26|         0.3234323|         0.7651515|       0.9898990|       0.5101010|
|      0.27|         0.3305228|         0.7741935|       0.9898990|       0.4848485|
|      0.28|         0.3462898|         0.8086957|       0.9898990|       0.4696970|
|      0.29|         0.3576642|         0.8173077|       0.9898990|       0.4292929|
|      0.30|         0.3677298|         0.8415842|       0.9898990|       0.4292929|
|      0.31|         0.3791103|         0.8571429|       0.9898990|       0.4242424|
|      0.32|         0.3920000|         0.8750000|       0.9898990|       0.3888889|
|      0.33|         0.4066390|         0.9047619|       0.9898990|       0.3838384|
|      0.34|         0.4197002|         0.9102564|       0.9898990|       0.3585859|
|      0.35|         0.4342984|         0.9189189|       0.9848485|       0.3434343|
|      0.36|         0.4490741|         0.9295775|       0.9797980|       0.3333333|
|      0.37|         0.4630072|         0.9384615|       0.9797980|       0.3080808|
|      0.38|         0.4743276|         0.9310345|       0.9797980|       0.2727273|
|      0.39|         0.4923469|         0.9454545|       0.9747475|       0.2626263|
|      0.40|         0.5079787|         0.9400000|       0.9646465|       0.2373737|
|      0.41|         0.5190217|         0.9574468|       0.9646465|       0.2272727|
|      0.42|         0.5264624|         0.9772727|       0.9545455|       0.2171717|
|      0.43|         0.5356125|         0.9750000|       0.9494949|       0.1969697|
|      0.44|         0.5535714|         0.9736842|       0.9393939|       0.1868687|
|      0.45|         0.5674847|         0.9696970|       0.9343434|       0.1616162|
|      0.46|         0.5854430|         0.9677419|       0.9343434|       0.1515152|
|      0.47|         0.6000000|         1.0000000|       0.9242424|       0.1363636|
|      0.48|         0.6122449|         1.0000000|       0.9090909|       0.1363636|
|      0.49|         0.6276596|         1.0000000|       0.8939394|       0.1363636|
|      0.50|         0.6490566|         1.0000000|       0.8686869|       0.1313131|
|      0.51|         0.6640625|         1.0000000|       0.8585859|       0.1161616|
|      0.52|         0.6720000|         1.0000000|       0.8484848|       0.1060606|
|      0.53|         0.6803279|         1.0000000|       0.8383838|       0.0909091|
|      0.54|         0.6962025|         1.0000000|       0.8333333|       0.0909091|
|      0.55|         0.7061404|         1.0000000|       0.8131313|       0.0909091|
|      0.56|         0.7272727|         1.0000000|       0.8080808|       0.0656566|
|      0.57|         0.7598039|         1.0000000|       0.7828283|       0.0606061|
|      0.58|         0.7743590|         1.0000000|       0.7626263|       0.0555556|
|      0.59|         0.7712766|         1.0000000|       0.7323232|       0.0454545|
|      0.60|         0.7868852|         1.0000000|       0.7272727|       0.0404040|
|      0.61|         0.8033708|         1.0000000|       0.7222222|       0.0404040|
|      0.62|         0.8192771|         1.0000000|       0.6868687|       0.0303030|
|      0.63|         0.8187500|         1.0000000|       0.6616162|       0.0303030|
|      0.64|         0.8421053|         1.0000000|       0.6464646|       0.0303030|
|      0.65|         0.8503401|         1.0000000|       0.6313131|       0.0252525|
|      0.66|         0.8571429|         1.0000000|       0.6060606|       0.0252525|
|      0.67|         0.8702290|         1.0000000|       0.5757576|       0.0252525|
|      0.68|         0.8880000|         1.0000000|       0.5606061|       0.0252525|
|      0.69|         0.8852459|         1.0000000|       0.5454545|       0.0252525|
|      0.70|         0.8898305|         1.0000000|       0.5303030|       0.0252525|
|      0.71|         0.8965517|         1.0000000|       0.5252525|       0.0202020|
|      0.72|         0.9150943|         1.0000000|       0.4898990|       0.0202020|
|      0.73|         0.9200000|         1.0000000|       0.4646465|       0.0202020|
|      0.74|         0.9444444|         1.0000000|       0.4292929|       0.0202020|
|      0.75|         0.9647059|         1.0000000|       0.4141414|       0.0151515|
|      0.76|         0.9753086|         1.0000000|       0.3989899|       0.0151515|
|      0.77|         0.9736842|         1.0000000|       0.3737374|       0.0101010|
|      0.78|         0.9701493|         1.0000000|       0.3282828|       0.0050505|
|      0.79|         0.9696970|         1.0000000|       0.3232323|       0.0050505|
|      0.80|         0.9655172|         1.0000000|       0.2828283|       0.0050505|
|      0.81|         0.9615385|         1.0000000|       0.2525253|       0.0050505|
|      0.82|         0.9782609|         1.0000000|       0.2272727|       0.0050505|
|      0.83|         0.9777778|         1.0000000|       0.2222222|       0.0050505|
|      0.84|         1.0000000|         1.0000000|       0.2171717|       0.0000000|
|      0.85|         1.0000000|         1.0000000|       0.1868687|       0.0000000|
|      0.86|         1.0000000|         1.0000000|       0.1717172|       0.0000000|
|      0.87|         1.0000000|         1.0000000|       0.1464646|       0.0000000|
|      0.88|         1.0000000|         1.0000000|       0.1313131|       0.0000000|
|      0.89|         1.0000000|         1.0000000|       0.1111111|       0.0000000|
|      0.90|         1.0000000|         1.0000000|       0.0858586|       0.0000000|
|      0.91|         1.0000000|         1.0000000|       0.0808081|       0.0000000|
|      0.92|         1.0000000|         1.0000000|       0.0707071|       0.0000000|
|      0.93|         1.0000000|         1.0000000|       0.0505051|       0.0000000|
|      0.94|         1.0000000|         1.0000000|       0.0505051|       0.0000000|
|      0.95|         1.0000000|         1.0000000|       0.0353535|       0.0000000|


:::
:::



## Visualizando o Dilema do Negócio (Trade-off)

O gráfico abaixo mostra como a Precisão (capacidade de evitar alarmes falsos) e o Recall (capacidade de capturar os alvos reais) se comportam conforme mudamos o rigor do modelo.


::: {.cell}
::: {.cell-output .cell-output-stderr}

```
Warning: Using `size` aesthetic for lines was deprecated in ggplot2 3.4.0.
ℹ Please use `linewidth` instead.
```


:::

::: {.cell-output-display}
![](02_classificacao_files/figure-html/grafico-tradeoff-1.png){width=672}
:::
:::



::: {.cell}
::: {.cell-output-display}
![Comparativo de Performance: Preto (Precisão) vs Vermelho (Recall)](02_classificacao_files/figure-html/grafico-tradeoff2-1.png){width=672}
:::
:::



## Aplicação no Mundo Real: Manutenção Preditiva

Imagine o custo de uma máquina parada por um erro do modelo:

- **Falso Positivo (Alarme Falso)**: Paramos a produção para manutenção, mas a peça estava boa. Custo: Mão de obra e perda de produção desnecessária.

- **Falso Negativo (Falha Não Detectada)**: O modelo disse que estava tudo bem, mas a máquina quebrou. Custo: Reparo emergencial caríssimo e parada não planejada.


**Perguntas para reflexão:**

- Se o custo de uma quebra (Falso Negativo) é 10x maior que o custo da inspeção, qual modelo você escolheria?

- Em qual threshold você operaria o Modelo A para garantir que não perderia nenhuma falha?
