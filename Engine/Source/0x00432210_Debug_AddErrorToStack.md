---
offset: "0x00432210"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Debug/ErrorStack.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00432210 — `Debug_AddErrorToStack`

- **Адрес (Offset):** `0x00432210`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Debug/ErrorStack.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00432210
Blizzard::Debug::ErrorStackRecord* Blizzard::Debug::AddErrorToStack(ErrorStackRecord* stack, int32_t errCode, const char* errStr, int32_t category) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00432210 в IDA Pro / Ghidra
