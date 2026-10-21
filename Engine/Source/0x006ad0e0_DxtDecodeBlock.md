---
offset: "0x006ad0e0"
module: "Engine/Source"
file: "Engine/Source/Gx/Blit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006ad0e0 — `DxtDecodeBlock`

- **Адрес (Offset):** `0x006ad0e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gx/Blit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ad0e0
void DxtDecodeBlock(const Dxt5Block* block, CArgb4444** rows, const DxtRect& rect, uint8_t (*alpha)(uint32_t)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ad0e0 в IDA Pro / Ghidra
