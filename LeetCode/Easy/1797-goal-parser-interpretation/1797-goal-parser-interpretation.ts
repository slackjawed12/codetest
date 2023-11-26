function interpret(command: string): string {
    const result = command.replace(/\(\)/g, "o").replace(/\(al\)/g, "al");

    return result;
};