# 최종 HTML/PDF 서식 적용 지시서 — Marie-style Report Layout Final

## 사용 목적

최종 보고서 원고의 **본문 내용은 수정하지 않고**, HTML/CSS를 이용해 최종 PDF를 만든다. DOCX는 이 파이프라인의 목표물이 아니다.

원본 문서:
- `13_FINAL_REPORT.md` 또는 사용자가 제공한 최종 보고서 MD

최종 산출물:
- `report.html`
- `report_style.css`
- `report.pdf`

---

## 1. 최상위 원칙

- 내용 손실 0%.
- 문장 재작성 금지.
- 제목 의미 변경 금지.
- 표·코드블록·소결·Watchlist 삭제 금지.
- 허용 작업은 HTML 구조화, CSS 서식, 표지 구성, PDF 렌더링, 시각 검수뿐이다.
- 최종 PDF 품질을 우선한다.
- DOCX와 동일 편집성을 목표로 하지 않는다.

---

## 2. 렌더링 방식

권장 파이프라인:

```text
13_FINAL_REPORT.md
        ↓
Markdown parser
        ↓
report.html + report_style.css
        ↓
Chromium / Playwright / WeasyPrint PDF renderer
        ↓
PDF 렌더링 검수
```

권장 렌더러:
- Chromium / Playwright / Puppeteer 계열
- 또는 WeasyPrint
- A4 print CSS 지원 필요

---

## 3. 페이지 설정

```css
@page:first { size: A4; margin: 0; }

@page {
  size: A4;
  margin: 24mm 24mm 22mm 24mm;
}
```

- 첫 페이지는 표지이므로 여백 0.
- 본문 페이지는 A4, 위 24mm, 아래 22mm, 좌우 24mm.
- PDF 출력 시 배경색과 선이 빠지지 않도록 `print-color-adjust: exact`를 사용한다.

---

## 4. 표지 레이아웃 — Marie-style Cover

표지는 HTML의 독립 `<section class="cover">`로 만든다.

필수 요소:
1. 상단 긴 가로선
2. 검은 정사각형 로고 박스
3. 로고 박스 내부 흰색 이니셜 마크
4. 문서 유형 라벨
5. 큰 제목 2줄
6. 작은 부제
7. 하단 왼쪽 세로 장식선

표지 제목은 반드시 굵은 볼드체로 처리한다. 단, 제목 크기·위치·부제·로고·소결 규칙 등 다른 확정 서식은 변경하지 않는다.

권장 CSS 좌표:

```css
.cover {
  width: 210mm;
  height: 297mm;
  position: relative;
  break-after: page;
}

.cover-rule-top {
  position: absolute;
  left: 20mm;
  right: 0;
  top: 32mm;
  border-top: 1.35pt solid #1f1f1f;
}

.cover-axis {
  position: absolute;
  left: 45mm;
}

.cover-logo {
  position: absolute;
  top: 62mm;
  width: 27mm;
  height: 27mm;
}

.cover-label {
  top: 94.5mm;
  font-size: 12.1pt;
  font-weight: 760;
}

.cover-title {
  top: 129mm;
  width: 140mm;
  font-size: 34pt;
  line-height: 1.02;
  font-weight: 800;
}

.cover-subtitle {
  top: 166.5mm;
  width: 140mm;
  font-size: 11.5pt;
  line-height: 1.28;
}

.cover-rule-vertical {
  position: absolute;
  left: 45mm;
  top: 210mm;
  height: 58mm;
  border-left: 1.15pt solid #1f1f1f;
}
```

---

## 5. 로고 마크 규칙

검은 정사각형 안의 `S.` 또는 이니셜 마크는 텍스트 마침표를 쓰지 않고 SVG로 만든다.

원칙:
- 대문자는 흰색 텍스트.
- 점은 흰색 **정사각형** 도형.
- 점의 오른쪽 끝은 검은 정사각형 오른쪽 변에 붙는다.
- 점 오른쪽에는 검은 테두리가 남지 않는다.
- 점은 알파벳 아래쪽 시각선과 각이 맞아야 한다.
- 아래로 처지거나 잘리면 안 된다.

권장 SVG:

```html
<svg viewBox="0 0 100 100" class="cover-logo-svg">
  <rect x="0" y="0" width="100" height="100" fill="#1f1f1f"/>
  <text x="65" y="55"
        text-anchor="middle"
        dominant-baseline="middle"
        font-family="Arial, Helvetica, sans-serif"
        font-size="74"
        fill="white">S</text>
  <rect x="91" y="70" width="9" height="9" fill="white"/>
</svg>
```

핵심:
- 점은 `<rect>`로 만든다.
- 점의 오른쪽 변을 붙이려면 `x + width = 100`이어야 한다.
- 예: `x="91" width="9"`.

---

## 6. 장 제목 스타일

각 주요 장 제목은 `<h2>`로 처리한다.

```css
.report-body h2 {
  font-size: 20.5pt;
  line-height: 1.18;
  font-weight: 800;
  margin: 0 0 6.5mm 0;
  padding: 0 0 2.2mm 0;
  border-bottom: 1.25pt solid #1f1f1f;
}
```

- 제목과 가로선 사이 간격은 1~3pt 수준으로 좁게 유지한다.
- 가로선은 별도 빈 문단이 아니라 제목의 하단 border로 처리한다.
- 주요 장은 필요하면 새 페이지에서 시작한다.

---

## 7. 소제목 스타일

```css
.report-body h3 {
  font-size: 14.3pt;
  line-height: 1.28;
  font-weight: 760;
  margin: 9mm 0 3.3mm 0;
}
```

- 소제목 위 간격은 충분히 둔다.
- 빈 줄을 직접 여러 번 넣지 않고 CSS margin으로 제어한다.

---

## 8. 본문 문단

```css
.report-body p {
  margin: 0 0 4.2mm 0;
  text-indent: 0.35cm;
  line-height: 1.52;
}
```

- 첫 줄 들여쓰기는 작게 한다.
- 표, 목록, 코드블록, 소결 박스 안에는 첫 줄 들여쓰기를 적용하지 않는다.
- 본문 글꼴은 `Noto Sans CJK KR`, `Malgun Gothic`, `Apple SD Gothic Neo`, Arial 계열을 사용한다.

---

## 9. 목록 스타일

점 목록이나 숫자 목록은 **마커와 글자가 함께 들여쓰기**되어야 한다.

```css
.report-body ul,
.report-body ol {
  margin: 3.5mm 0 5mm 0;
  padding-left: 7.5mm;
  list-style-position: outside;
}

.report-body li {
  margin: 0 0 2mm 0;
  padding-left: 1.2mm;
  text-indent: 0;
}
```

금지:
- `li`에 본문 문단용 `text-indent`를 적용하지 않는다.
- 마커는 왼쪽에 남고 글자만 오른쪽으로 밀리는 hanging 형태를 만들지 않는다.

---

## 10. 표 스타일

```css
.report-body table {
  width: 94%;
  margin: 6mm auto 8mm auto;
  border-collapse: collapse;
  table-layout: fixed;
  font-size: 9.2pt;
}

.report-body th,
.report-body td {
  border: 0.75pt solid #d9d9d9;
  padding: 3mm 3.2mm;
  vertical-align: top;
}

.report-body th {
  background: #eeeeee;
  font-weight: 800;
  text-align: center;
}

.report-body td {
  text-align: left;
}
```

- 표 자체는 본문 영역 기준 가운데 정렬한다.
- 표 내부 본문 셀은 기본 왼쪽 정렬한다.
- 짧은 판정값도 열마다 흔들리지 않게 왼쪽 정렬한다.
- 숫자만 들어가는 열만 예외적으로 가운데 정렬할 수 있다.

---

## 11. 코드블록 / 설정블록

```css
.report-body pre {
  width: 94%;
  margin: 5mm auto 7mm auto;
  padding: 4mm 4.5mm;
  border: 0.75pt solid #d6d6d6;
  background: #f5f5f5;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  font-family: Consolas, Menlo, Courier New, monospace;
  font-size: 9pt;
  line-height: 1.36;
}
```

- 코드블록은 페이지 밖으로 나가면 안 된다.
- 긴 줄은 줄바꿈한다.

---

## 12. 소결 박스

`소결:` 또는 `**소결:**`로 시작하는 문단은 일반 문단이 아니라 callout box로 변환한다.

```css
.report-body .conclusion-box {
  width: 94%;
  margin: 5mm auto 7mm auto;
  padding: 3.4mm 4.3mm 3.4mm 5mm;
  border: 0.75pt solid #dedede;
  border-left: 3.2pt solid #1f1f1f;
  background: #f3f3f3;
  line-height: 1.48;
}

.report-body .conclusion-box strong {
  font-weight: 800;
  display: inline-block;
  margin-right: 4.5mm;
}
```

- `소결` 라벨은 굵게.
- `소결` 뒤 설명문과의 거리는 `margin-right`로 확보한다.
- 회색 배경 + 왼쪽 검은 세로선.
- 첫 줄 들여쓰기 없음.

---

## 13. 최종 검수

PDF 생성 후 반드시 렌더링 이미지로 확인한다.

검수 항목:
- 표지 상단선 위치가 기준 표지와 과하게 다르지 않은가?
- 로고 점이 흰색 정사각형인가?
- 로고 점의 오른쪽 변이 검은 사각형 오른쪽 변에 붙어 있는가?
- 점 오른쪽에 검은 테두리가 남지 않는가?
- 로고 글자가 아래로 처지거나 잘리지 않는가?
- 표지 제목과 부제가 충분히 큰가?
- 표지 제목은 굵은 볼드체로 보이는가?
- 장 제목 밑줄이 제목과 너무 멀지 않은가?
- 본문 첫 줄 들여쓰기가 과하지 않은가?
- 목록의 점/숫자와 글자 사이가 벌어지지 않는가?
- 표가 가운데 정렬되는가?
- 표 셀 내부 정렬이 일관적인가?
- 코드블록이 페이지 밖으로 나가지 않는가?
- 소결 박스가 회색 배경 + 왼쪽 검은 선으로 보이는가?
- `소결` 라벨과 설명문 사이에 적절한 간격이 있는가?
- 불필요한 빈 페이지가 없는가?