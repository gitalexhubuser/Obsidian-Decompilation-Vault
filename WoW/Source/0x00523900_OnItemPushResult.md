---
offset: "0x00523900"
module: "WoW/Source"
file: "WoW/Source/Ui/GameUI.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00523900 — `OnItemPushResult`

- **Адрес (Offset):** `0x00523900`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/GameUI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00523900
void OnItemPushResult(WOWGUID guid, uint8_t bag, uint32_t slot, uint32_t itemId, uint32_t suffixFactor, uint32_t randomPropertyId, uint32_t received, uint32_t created, uint32_t showInChat, uint32_t count) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00523900 в IDA Pro / Ghidra
