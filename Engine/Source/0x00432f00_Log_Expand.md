---
offset: "0x00432f00"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Log/Log.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00432f00 — `Log_Expand`

- **Адрес (Offset):** `0x00432f00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Log/Log.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00432f00
bool Blizzard::Log::Expand(int32_t logClass, const char* name, char* dst, int32_t count, bool createDirectory) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00432f00 в IDA Pro / Ghidra
