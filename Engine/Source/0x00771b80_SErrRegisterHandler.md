---
offset: "0x00771b80"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SErr.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00771b80 — `SErrRegisterHandler`

- **Адрес (Offset):** `0x00771b80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SErr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00771b80
void STORMAPI SErrRegisterHandler(int32_t (STORMAPI* handler)(uint32_t, const char*, const char*, int32_t, const char*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00771b80 в IDA Pro / Ghidra
