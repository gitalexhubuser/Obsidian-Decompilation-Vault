---
offset: "0x00438560"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Log/Log.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00438560 — `System_Log_Reopen`

- **Адрес (Offset):** `0x00438560`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Log/Log.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00438560
bool System_Log::Reopen(int32_t logClass, const char* name, FILE*& file, int32_t& index, bool binary) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00438560 в IDA Pro / Ghidra
