---
offset: "0x00767030"
module: "Engine/Source"
file: "Engine/Source/ConsoleBase/ConsoleVar.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00767030 — `CVar_IterateForArchive`

- **Адрес (Offset):** `0x00767030`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ConsoleBase/ConsoleVar.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00767030
int32_t CVar::IterateForArchive(uint32_t category, uint32_t excludeFlags, int32_t (*callback)(const char* name, const char* value, void* arg), void* arg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00767030 в IDA Pro / Ghidra
