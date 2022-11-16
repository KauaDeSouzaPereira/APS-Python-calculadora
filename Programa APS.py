import math


print('--------------------------------------------------------------------------')
print('-                   ----                                                 -')
print('-                  ---                                                   -')
print('-   -------     -----    ---      -------    ---  ---   ---      ------- -')
print('-   -------    -------   ---      -------    ---  ---   ---      ------- -')
print('-   --         --   --   ---      --         ---  ---   ---      --   -- -')
print('-   --         -------   ---      --         ---  ---   ---      --   -- -')
print('-   -------    --   --   -------  -------    --------   -------  ------- -')
print('-   -------    --   --   -------  -------      ----     -------  ------- -')
print('--------------------------------------------------------------------------')









valcobustive = 0



emissaoCigarro = input('Sua empresa trabalha com cigarros? Responda s ou n ')
if emissaoCigarro == 's':
    qtsCigarro = int(input('Quantos cigarros sua empresa vende por mês? '))
    valCigarro = qtsCigarro * 0.14

energiaEletric = float(input('Quanto que a sua empresa gasta de KWH por mês? Responda em números '))
valEletric = energiaEletric * 0.190

distribuicao = input('Sua empresa realiza a distribuição por conta própria? Responda s ou n ')
if distribuicao == 's':
    qtscaminhoes = int(input('Quantas entregas sua empresa faz por mês? Responda em números '))
    valcombustivel = qtscaminhoes * 300 


totalCarb = (valCigarro + valEletric + valcombustivel) * 12

print('Sua empresa gasta: ', totalCarb, 'quilos de carbono')

retrasado = float(input('Qual foi a emissão de carbono da sua empresa no ano retrasado? Responda em números'))
retrasado = retrasado - totalCarb

if retrasado > 0 :
    print('Você lucrou', retrasado ,'este ano')
    vender = input('Você deseja vender o seu crédito de carbono para outras empresas? Responda s ou n ')
    if vender == 's':
      op = int(input('Essas são as empresas que nós sugerimos para você: 1-Apple, 2-O boticario, 3-Amazon ou 4-Ifood. Responda usando 1, 2, 3 , 4 '))
    if op == 1:
      print('https://www.apple.com/br/?afid=p238%7CswLlkpYLw-dc_mtid_1870765e38482_pcrid_634503065735_pgrid_105601108225_pntwk_g_pchan__pexid__&cid=aos-br-kwgo-brand--slid---product-')
    if op == 2:
      print('https://www.boticario.com.br/?&utm_source=google&utm_medium=cpc&utm_campaign=18281460401_137894085741&ds_rl=1270144&gclid=CjwKCAiA68ebBhB-EiwALVC-NmsFbK_7z6WJ4Z7FGmNg8vJ2Svzsu0F-3CPxWgno1jhIURwUuccBNBoC_1AQAvD_BwE&gclsrc=aw.ds')
    if op == 3:
      print('https://www.amazon.com.br/?tag=hydrbrgk-20&hvadid=558683589546&hvpos=&hvexid=&hvnetw=g&hvrand=9695004996668470602&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001655&hvtargid=kwd-15305691825&ref=pd_sl_7ddjoi3zeb_e')
    if op == 4:
      print('https://parceiros.ifood.com.br/restaurante/como-funciona?network=g&utm_source=google&utm_medium=cpc&utm_campaign=ifood_br_b2b_g-search_rmkt_black-friday-22&utm_content=633951469625&utm_term=ifood%20para%20restaurantes-b&gclid=CjwKCAiA68ebBhB-EiwALVC-NjUy4df75ZJKnQEHjJtSY8HpWVDcwxGO2Pv2lZenBFvvJmkGZ3I8_RoCTTAQAvD_BwE')

if retrasado < 0 :
  print('Você teve um prejuizo de',retrasado,'este ano')
  comprar = input('Você deseja comprar crédito de carbono ou plantar árvores? Responda 1 - crédito de carbono ou 2 - plantar árvores  ')
  if comprar == '1':
    retrasado = (retrasado /1000) *-1
    print('Para compensar a sua emissão você vai ter que comprar',retrasado,'créditos, que serião U$',retrasado * 10,'dolares')
  if comprar == '2':
    retrasado = (retrasado /1000) *-8
    print('Para compensar a sua emissão você vai ter que plantar',math.ceil(retrasado),'árvores')
if retrasado == 0 :
  print('Sua emissão não alterou.')
