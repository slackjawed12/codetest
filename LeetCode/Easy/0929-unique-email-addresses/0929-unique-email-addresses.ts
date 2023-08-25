function numUniqueEmails(emails: string[]): number {
    return emails.reduce((prev,cur)=>{
        const [local, domain] = cur.split('@');
        const nonplus = local.split('+')[0];
        const convertedEmail = nonplus.split('.').join('').concat('@'+domain);
        
        prev.add(convertedEmail);
        return prev;
    }, new Set<string>()).size;
};