---
offset: "0x00771900"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SErr.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00771900 — `SErrSetLogCallback`

- **Адрес (Offset):** `0x00771900`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SErr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00771900
void STORMAPI SErrSetLogCallback(int32_t (STORMAPI* callback)(char*, uint32_t)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00771900 в IDA Pro / Ghidra
