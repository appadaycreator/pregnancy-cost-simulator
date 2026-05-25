LEGACY_HTML = True  # 既存HTMLを保持（再アセンブル禁止）
TITLE = '出産費用計算【無料】妊娠から産後まで総額いくかかる？'
DESCRIPTION = '出産方式・病院・地域から妊娠〜産後までの総費用を無料計算。出産一時金・補助金も考慮。'
JS_CODE = "var birthCosts={natural:{public:350000,private:500000,premium:700000},painless:{public:500000,private:650000,premium:900000},cesarean:{public:450000,private:580000,premium:780000}};\nfunction calculate(){\n  var bt=document.getElementById('birth-type').value;\n  var ht=document.getElementById('hospital-type').value;\n  var pm=parseInt(document.getElementById('prenatal-months').value)||9;\n  var goods=(parseFloat(document.getElementById('baby-goods').value)||20)*10000;\n  var childcareMonthly=(parseFloat(document.getElementById('childcare-monthly').value)||5)*10000;\n  var birthCost=birthCosts[bt][ht];\n  var checkupCost=pm*10000;\n  var childcareCost=childcareMonthly*6;\n  var total=birthCost+checkupCost+goods+childcareCost;\n  var net=total-500000;\n  document.getElementById('r-total').textContent='約'+Math.round(total/10000)+'万円';\n  document.getElementById('r-birth').textContent=Math.round(birthCost/10000)+'万円';\n  document.getElementById('r-checkup').textContent=Math.round(checkupCost/10000)+'万円';\n  document.getElementById('r-goods').textContent=Math.round(goods/10000)+'万円';\n  document.getElementById('r-childcare').textContent=Math.round(childcareCost/10000)+'万円';\n  document.getElementById('r-net').textContent=net>0?'自己負担 約'+Math.round(net/10000)+'万円':'一時金内に収まります！';\n  document.getElementById('r-net-note').textContent=net>0?'出産育児一時金（50万円）を超える費用が自己負担になります':'おめでとうございます。一時金（50万円）で賄える見込みです';\n  var advice='';\n  if(bt==='cesarean'){advice='帝王切開は健康保険適用のため、高額療養費制度も利用できます。事前に限度額適用認定証を取得しておくと窓口負担を抑えられます。';}\n  else if(ht==='premium'){advice='プレミアム病院は快適ですが費用が高めです。自治体の補助金・出産準備金も確認しておきましょう。';}\n  else{advice='自治体によっては妊婦健診の補助券が使えます。お住まいの市区町村の補助金制度もご確認ください。';}\n  document.getElementById('r-advice').textContent='💡 '+advice;\n  document.getElementById('results').style.display='block';\n  document.getElementById('affiliate-section').style.display='block';\n  document.getElementById('results').scrollIntoView({behavior:'smooth'});\n}"
MAIN_HTML = '<div><button class="btn">開始する</button></div>'
FAQ = [
    ('出産費用計算は無料で使えますか？', 'はい、完全無料・登録不要でご利用いただけます。'),
    ('何回でも使えますか？', 'はい、回数制限なく何度でもご利用いただけます。'),
    ('入力したデータはサーバーに送信されますか？', 'いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。'),
    ('スマートフォンでも使えますか？', 'はい、スマートフォン・タブレット・PCすべてに最適化されています。'),
    ('結果を保存・共有できますか？', 'スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。'),
]
HOW_TO = [
    'ページを開き、入力フォームの項目を確認する',
    '必要な情報を入力または選択する',
    '実行ボタンをクリックして結果を取得する',
    '表示された結果・アドバイスを確認する',
    '必要に応じてコピー・SNSシェアで活用する',
]
FOOTER_LINKS = [('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー'), ('https://appadaycreator.com/bmi-body-tracker/', 'BMI・体重管理'), ('https://appadaycreator.com/household-budget-analyzer/', '家計簿診断')]
