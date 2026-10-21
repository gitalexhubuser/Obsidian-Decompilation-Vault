---
offset: "0x0050cfc0"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0050cfc0 — `CGChat_HandleFlagsChanged`

- **Адрес (Offset):** `0x0050cfc0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0050cfc0
void CGChat::HandleFlagsChanged(WOWGUID guid, uint8_t oldFlags, uint8_t newFlags, const char* channel) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0050cfc0 в IDA Pro / Ghidra
