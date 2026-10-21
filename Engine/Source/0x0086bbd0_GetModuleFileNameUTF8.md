---
offset: "0x0086bbd0"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/Path.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086bbd0 — `GetModuleFileNameUTF8`

- **Адрес (Offset):** `0x0086bbd0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/Path.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086bbd0
uint32_t GetModuleFileNameUTF8(void* module, char* path, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086bbd0 в IDA Pro / Ghidra
