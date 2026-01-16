export const renderTemplate = (template: string, variables: Record<string, any>): string => {
    return template.replace(/\{\{(.*?)\}\}/g, (_, rawKey) => {
        const key = rawKey.trim();
        const value = variables[key];
        if (value === undefined || value === null) {
            return '';
        }
        return String(value);
    });
};
