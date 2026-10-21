---
offset: "0x005204c0"
module: "WoW/Source"
file: "WoW/Source/Ui/GameUI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x005204c0 — `CGGameUI_NewZoneFeedback`

- **Адрес (Offset):** `0x005204c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GameUI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x005204c0
void CGGameUI::NewZoneFeedback(int32_t areaId, int32_t subzoneId, int32_t wmoGroupId, const char* zoneText, const char* subZoneText, const char* realZoneText, int32_t inside) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x005204c0 в IDA Pro / Ghidra
