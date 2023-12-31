function capitalizeTitle(title: string): string {
  const words = title.split(" ");

  return words
    .map((word) => {
      if (word.length === 1 || word.length === 2) {
        return word.toLowerCase();
      }

      const lower = word.toLowerCase();
      const upperHead = word[0].toUpperCase();
      return upperHead.concat(lower.slice(1));
    })
    .join(" ");
}
