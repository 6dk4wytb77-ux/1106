from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION

out='PRD_個人學習行程與任務管理系統.docx'
doc=Document()
sec=doc.sections[0]
sec.top_margin=Inches(.72); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.8); sec.right_margin=Inches(.8)
styles=doc.styles
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3']:
    st=styles[name]; st.font.name='Microsoft JhengHei'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei'); st.font.color.rgb=RGBColor(0,0,0)
styles['Normal'].font.size=Pt(10.5); styles['Normal'].paragraph_format.space_after=Pt(5)
styles['Title'].font.size=Pt(26); styles['Title'].font.bold=True; styles['Title'].paragraph_format.space_after=Pt(4)
styles['Subtitle'].font.size=Pt(12); styles['Subtitle'].font.color.rgb=RGBColor(85,100,90); styles['Subtitle'].paragraph_format.space_after=Pt(14)
for nm,size in [('Heading 1',16),('Heading 2',12),('Heading 3',10.5)]:
 st=styles[nm];st.font.size=Pt(size);st.font.bold=True;st.paragraph_format.space_before=Pt(12 if nm=='Heading 1' else 8);st.paragraph_format.space_after=Pt(4);st.paragraph_format.keep_with_next=True

def shade(cell,color):
 tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd');shd.set(qn('w:fill'),color);tcPr.append(shd)
def borders(table):
 tblPr=table._tbl.tblPr; b=OxmlElement('w:tblBorders')
 for edge in ('top','left','bottom','right','insideH','insideV'):
  e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'5');e.set(qn('w:space'),'0');e.set(qn('w:color'),'D9E0DB');b.append(e)
 tblPr.append(b)
def set_cell(cell,text,bold=False,color=None,size=9.3):
 cell.text='';p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);r=p.add_run(str(text));r.bold=bold;r.font.name='Microsoft JhengHei';r._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');r.font.size=Pt(size)
 if color:r.font.color.rgb=RGBColor(*color)
 cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

def table(headers, rows, widths=None):
 t=doc.add_table(rows=1, cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 if widths:
  for c,w in zip(t.columns,widths):c.width=Inches(w)
 for i,h in enumerate(headers):set_cell(t.rows[0].cells[i],h,True,(255,255,255),9);shade(t.rows[0].cells[i],'496E59')
 for ri,row in enumerate(rows):
  cells=t.add_row().cells
  for i,val in enumerate(row):set_cell(cells[i],val,size=9)
  if ri%2==1:
   for c in cells:shade(c,'F4F7F4')
  if widths:
   for c,w in zip(cells,widths):c.width=Inches(w)
 borders(t);doc.add_paragraph().paragraph_format.space_after=Pt(0)
 return t

def para(text='',boldlead=None):
 p=doc.add_paragraph()
 if boldlead and text.startswith(boldlead):p.add_run(boldlead).bold=True;p.add_run(text[len(boldlead):])
 else:p.add_run(text)
 return p

# Header/footer
header=sec.header.paragraphs[0];header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=header.add_run('產品需求文件  |  個人學習管理');r.font.name='Microsoft JhengHei';r._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');r.font.size=Pt(8);r.font.color.rgb=RGBColor(120,130,122)
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=footer.add_run('拾光 Study Planner  ·  PRD  ·  2026-10-30');r.font.name='Microsoft JhengHei';r._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei');r.font.size=Pt(8);r.font.color.rgb=RGBColor(130,138,132)

p=doc.add_paragraph(style='Title');p.add_run('個人學習行程與任務管理系統')
p=doc.add_paragraph(style='Subtitle');p.add_run('產品需求文件（PRD）｜第一版前端原型範圍')
para('本文件定義「拾光」第一版的產品目標、使用者需求、核心互動與驗收條件。產品以個人學習規劃為核心，支援桌機與手機，讓使用者能分別檢視今日、每週與所有學習任務，並以優先順序協助決定先做什麼。')
table(['文件資訊','內容'],[['產品名稱','拾光（暫定）'],['文件版本','1.0'],['日期','2026 年 10 月 30 日'],['產品型態','響應式網頁前端原型'],['目標使用者','需要安排課程、自主學習、複習與考試準備的個人使用者']],[1.45,5.35])

doc.add_heading('1. 產品概述',level=1)
para('拾光是一套輕量的個人學習行程與任務管理系統。它將固定時段的學習安排、具截止日期的學習目標與彈性待辦集中管理，讓使用者可以快速掌握今天的學習計畫、瀏覽整週節奏、追蹤完成進度。')
para('第一版以單機瀏覽器體驗為主，任務資料保存於瀏覽器 localStorage。這可滿足原型的重新整理後資料留存需求，但不提供跨裝置同步、帳號或雲端備份。')
doc.add_heading('2. 問題與機會',level=1)
para('學習者常將固定課程、讀書時段與待辦事項分散在不同工具，難以從每日視角判斷優先順序，也不容易同時檢視一週負荷。產品以今日清單與週行程作為主要入口，提供科目分類、優先級、時間欄位與完成狀態，降低安排及追蹤成本。')
doc.add_heading('3. 產品目標與非目標',level=1)
table(['類別','定義'],[['目標','快速查看今天要做的學習任務與時間安排'],['目標','以週總覽掌握任務分布，支援前後週瀏覽'],['目標','透過高／中／低優先順序協助排序與聚焦'],['目標','用完整表單記錄任務資訊，並在同一瀏覽器保留資料'],['非目標（第一版）','帳號註冊、雲端同步、多裝置資料合併'],['非目標（第一版）','推播、Email、行事曆整合與週期性任務自動產生'],['非目標（第一版）','學習分析報表、多人協作、AI 自動排程']],[1.5,5.3])
doc.add_heading('4. 使用者與核心情境',level=1)
para('主要使用者是以個人方式安排學習計畫的學生或自學者。典型情境包括：開始一天時查看今日安排；規劃下週課程、複習和考試準備；新增一筆有截止日或固定時段的任務；完成任務後更新狀態；依科目或未完成狀態檢視任務。')
doc.add_heading('5. 資訊架構與頁面',level=1)
table(['工作區','用途與主要內容'],[['今日學習','當日任務清單、日期導覽、今日完成進度與學習時間摘要；切換日期查看該日任務。'],['週行程','獨立週總覽頁；以 7 日欄位顯示每一天的任務卡片；可切換前一週、下一週或回到本週。點日期進入該日行程，點任務開啟編輯。'],['所有任務','完整任務清單；支援科目與完成狀態篩選；可以切換完成狀態及編輯任務。'],['科目分類','側欄顯示分類與未完成數量；可新增分類，選取分類後進入所有任務並套用該分類篩選。']],[1.45,5.35])
para('導覽行為：桌機透過左側導覽列切換頁面；手機將導覽列固定於底部。每個工作區只顯示其自身頁面內容，當前導覽項目需有清楚的選取狀態。')
doc.add_heading('6. 功能需求',level=1)
table(['ID','需求','優先級','驗收條件'],[['FR-01','工作區導覽','必須','點選今日學習、週行程、所有任務時，顯示對應獨立頁面並更新目前導覽狀態。'],['FR-02','建立任務','必須','可由建立任務入口開啟完整表單；成功儲存後，任務出現在所選日期及所有任務清單。'],['FR-03','編輯任務','必須','可從任務卡片進入表單；儲存後更新既有任務，完成狀態維持不變。'],['FR-04','任務欄位','必須','支援名稱、科目、優先級、學習日期、截止日、開始／結束時間、預估分鐘、備註與完成狀態。'],['FR-05','欄位驗證','必須','名稱、科目、優先級及學習日期必填；結束時間需晚於開始時間；截止日期不得早於學習日期。'],['FR-06','完成狀態','必須','可切換完成／未完成；狀態更新後即時反映於任務列、統計與進度。'],['FR-07','週行程','必須','呈現所選週 7 日任務；可前後切換並回到本週；任務可編輯，點日期可前往該日。'],['FR-08','所有任務篩選','必須','可依科目與完成狀態篩選；無符合項目時顯示清楚空狀態。'],['FR-09','新增科目','應有','可建立非空且不重複的分類名稱，並於任務表單可選。'],['FR-10','本機保存','必須','新增、編輯、完成狀態及科目異動寫入 localStorage；重新整理同一瀏覽器後資料仍可讀取。'],['FR-11','響應式版面','必須','桌機使用側欄；手機使用底部導覽，週總覽可水平滑動，表單可在窄螢幕操作。']],[.55,1.35,.65,4.25])
doc.add_heading('7. 任務資料欄位與規則',level=1)
table(['欄位','型態','規則'],[['任務名稱','文字','必填，最多 80 字'],['科目／分類','文字／選項','必填，從使用者科目清單選擇'],['優先順序','列舉','必填；高、中、低，預設中'],['學習日期','日期','必填，代表預定進行任務的日期'],['截止日期','日期','選填；若有填寫，不可早於學習日期'],['開始／結束時間','時間','選填；若兩者均有填寫，結束時間需晚於開始時間'],['預估時間','整數分鐘','選填，最小 5、最大 1440，間隔 5 分鐘'],['備註','文字','選填，最多 500 字'],['完成狀態','布林','新增時預設未完成；編輯時保留現有狀態']],[1.35,1.2,4.25])
doc.add_heading('8. 主要使用流程',level=1)
doc.add_heading('8.1 新增學習任務',level=2)
para('使用者選擇「建立任務」→填寫完整表單→系統檢核必要欄位與時間／日期規則→儲存至本機→關閉表單並顯示新任務；若新增日期不在目前週範圍，週檢視應自動調整至該任務所在週。')
doc.add_heading('8.2 由週檢視前往單日',level=2)
para('使用者選擇「週行程」→瀏覽七日任務分布→點選日期→進入今日學習工作區並顯示該日清單；點選任務則開啟其編輯表單。')
doc.add_heading('8.3 完成任務',level=2)
para('使用者點選任務完成控制項→狀態立即更新並保存→今日進度、完成數與分類未完成數同步更新。')
doc.add_heading('9. UI／UX 原則',level=1)
for x in ['桌機與手機均可使用，優先確保主要任務操作在窄螢幕清楚易點。','今日、週行程、所有任務採獨立工作區，避免多個檢視混在同一頁造成資訊負荷。','高、中、低優先級使用可辨識的文字標籤與一致的色彩，而非只以顏色表達。','空狀態提供下一步建議；表單錯誤應在欄位附近以文字說明。','儲存或完成任務後提供即時回饋，並維持合理的導覽位置。']:
 p=doc.add_paragraph(style='List Bullet');p.add_run(x)
doc.add_heading('10. 非功能需求與限制',level=1)
table(['面向','要求／限制'],[['相容性','現代桌面與手機瀏覽器；介面使用響應式 CSS。'],['資料持久性','同一瀏覽器、同一來源的 localStorage；清除網站資料或使用其他瀏覽器可能造成資料遺失。'],['安全性與隱私','原型資料留在本機瀏覽器，不上傳伺服器；不應存放敏感個資。'],['可用性','主要操作可透過鍵盤與觸控完成；按鈕需具明確標籤。'],['外部相依','Google Fonts 用於字型呈現；離線時採系統字型回退。'],['原型限制','目前為前端原型，無後端、帳號、多裝置同步、備份與復原機制。']],[1.35,5.45])
doc.add_heading('11. 成功指標（後續產品化建議）',level=1)
para('目前尚無實際使用數據，建議正式測試時追蹤下列指標，先建立基準值後再設定目標：')
table(['指標','定義'],[['任務建立完成率','開始新增任務後成功儲存的比例'],['週檢視使用率','活躍使用者中曾進入週行程頁的比例'],['任務完成率','指定期間內已完成任務數／建立任務總數'],['回訪率','使用者在首次使用後 7 日內再次開啟產品的比例'],['表單錯誤率','發生欄位驗證錯誤的表單提交次數／提交總次數']],[1.7,5.1])
doc.add_heading('12. 風險與待確認事項',level=1)
table(['議題','目前處理／建議'],[['跨裝置資料','本機儲存不會自動同步；若多裝置使用是正式需求，需規劃登入、雲端資料庫及同步衝突策略。'],['資料安全與備份','目前沒有匯出、匯入或復原；正式使用前建議加入 JSON 備份與還原功能。'],['時區與日期','日期以本機瀏覽器時區處理；若加入伺服器同步，需定義時區標準與日期轉換規則。'],['週起始日','原型以週一作為每週起始日；產品化前可允許使用者設定。'],['提醒通知','尚未涵蓋提醒。需另行確認通知方式、提前時間、重複規則與授權體驗。']],[1.45,5.35])
doc.add_heading('13. 發布範圍摘要',level=1)
para('第一版交付可操作的響應式前端原型，涵蓋今日學習、週行程、所有任務、完整任務表單、優先級、科目分類、狀態切換及瀏覽器本機保存。此版本用於需求驗證與介面討論，不代表已具備正式服務所需的帳號、同步、備份、提醒或伺服器端資料保護能力。')

doc.save(out)
print(out)
