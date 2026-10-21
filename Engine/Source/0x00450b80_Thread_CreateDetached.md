---
offset: "0x00450b80"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Thread/ThreadAPI.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00450b80 — `Thread_CreateDetached`

- **Адрес (Offset):** `0x00450b80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Thread/ThreadAPI.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00450b80
bool Blizzard::Thread::CreateDetached(uint32_t (*function)(void*), void* param, const char* name) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00450b80 в IDA Pro / Ghidra
