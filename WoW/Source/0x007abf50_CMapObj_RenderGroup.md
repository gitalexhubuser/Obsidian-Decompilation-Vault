---
offset: "0x007abf50"
module: "WoW/Source"
file: "WoW/Source/WorldClient/MapObj.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007abf50 — `CMapObj_RenderGroup`

- **Адрес (Offset):** `0x007abf50`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WorldClient/MapObj.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007abf50
void CMapObj::RenderGroup(int32_t groupIndex, C44Matrix& matrix, TSExplicitList<CWFrustum, offsetof(CWFrustum, m_link)>* frustumList) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007abf50 в IDA Pro / Ghidra
