package com.rimworld.trainer;

import com.rimworld.trainer.features.GodMode;
import com.rimworld.trainer.features.InfiniteResources;

public class Main {
    public static void main(String[] args) {
        System.out.println("RimWorld Trainer - Initializing...");

        GodMode.enable();
        InfiniteResources.enable();

        System.out.println("Trainer features enabled. Press Ctrl+C to exit.");
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            GodMode.disable();
            InfiniteResources.disable();
            System.out.println("Trainer features disabled.");
        }));
    }
}