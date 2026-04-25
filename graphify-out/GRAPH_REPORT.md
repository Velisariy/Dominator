# Graph Report - Dominator  (2026-04-26)

## Corpus Check
- 7 files · ~4,531 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 42 nodes · 34 edges · 13 communities detected
- Extraction: 71% EXTRACTED · 29% INFERRED · 0% AMBIGUOUS · INFERRED: 10 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]

## God Nodes (most connected - your core abstractions)
1. `Dominator Project` - 9 edges
2. `Sidebar Navigation Panel` - 6 edges
3. `File Open Dialog` - 5 edges
4. `Application Icon` - 3 edges
5. `Dominator Application` - 3 edges
6. `reportlab` - 2 edges
7. `Dominant Color Detection` - 2 edges
8. `PDF Output` - 2 edges
9. `Exit Icon` - 2 edges
10. `Exit Symbol (X)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Dominator Project` --implements--> `Dominant Color Detection`  [INFERRED]
  AGENTS.md → hello.html
- `Dominator Project` --requires--> `reportlab`  [EXTRACTED]
  AGENTS.md → requirements.txt
- `Dominator Project` --implements--> `GUI Interface`  [INFERRED]
  AGENTS.md → hello.html
- `Dominator Project` --requires--> `Pillow`  [EXTRACTED]
  AGENTS.md → requirements.txt
- `Dominator Project` --requires--> `PyQt6`  [EXTRACTED]
  AGENTS.md → requirements.txt

## Hyperedges (group relationships)
- **Core Dependencies** — pillow, pyqt6, reportlab [EXTRACTED 1.00]
- **Quick Access Navigation Locations** — nav_recent, nav_home, nav_desktop, nav_documents, nav_downloads [EXTRACTED 1.00]
- **File Dialog Action Buttons** — action_open, action_cancel, action_new_folder [EXTRACTED 1.00]
- **Icon Composition** — icon_image, crown_symbol, dominator_text, server_text [EXTRACTED 0.95]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (7): Dominator Project, graphify Knowledge Graph, GUI Interface, Pillow, PyQt6, Python 3.x, Welcome UI Documentation

### Community 1 - "Community 1"
Cohesion: 0.33
Nodes (6): Cancel Button, New Folder Action, Open Button, File Listing Area, File Open Dialog, File Dialog Toolbar

### Community 2 - "Community 2"
Cohesion: 0.33
Nodes (6): Desktop Directory, Documents Directory, Downloads Directory, Home Directory, Recent Locations, Sidebar Navigation Panel

### Community 3 - "Community 3"
Cohesion: 0.4
Nodes (5): Dark Gray Background, Exit Icon, Exit Symbol (X), Rounded Square Container, White Symbol

### Community 4 - "Community 4"
Cohesion: 0.6
Nodes (5): Crown Symbol, Dominator Application, Dominator Text, Application Icon, SERVER Text

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (2): PDF Output, reportlab

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (2): Dominant Color Detection, Image Processing

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (2): Green Action Button, Save Button Icon

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (1): Refresh Icon

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (1): Визуальная оболочка для вычисления доминирующих цветов в изображении

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (1): Сравнение цвета со средним значением     для читабельного отображения текста

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (1): Визуальная оболочка для вычисления доминирующих цветов в изображении

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (1): Сравнение цвета со средним значением     для читабельного отображения текста

## Knowledge Gaps
- **24 isolated node(s):** `Визуальная оболочка для вычисления доминирующих цветов в изображении`, `Сравнение цвета со средним значением     для читабельного отображения текста`, `Визуальная оболочка для вычисления доминирующих цветов в изображении`, `Сравнение цвета со средним значением     для читабельного отображения текста`, `Python 3.x` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (2 nodes): `PDF Output`, `reportlab`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (2 nodes): `Dominant Color Detection`, `Image Processing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 7`** (2 nodes): `Green Action Button`, `Save Button Icon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (1 nodes): `Refresh Icon`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `Визуальная оболочка для вычисления доминирующих цветов в изображении`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `Сравнение цвета со средним значением     для читабельного отображения текста`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `Визуальная оболочка для вычисления доминирующих цветов в изображении`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `Сравнение цвета со средним значением     для читабельного отображения текста`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Dominator Project` connect `Community 0` to `Community 5`, `Community 6`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `Sidebar Navigation Panel` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `File Open Dialog` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Dominator Project` (e.g. with `Dominant Color Detection` and `GUI Interface`) actually correct?**
  _`Dominator Project` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Визуальная оболочка для вычисления доминирующих цветов в изображении`, `Сравнение цвета со средним значением     для читабельного отображения текста`, `Визуальная оболочка для вычисления доминирующих цветов в изображении` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._