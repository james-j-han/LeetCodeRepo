class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # set(unique emails to occurrences)

        # loop through emails array and split email on @ symbol and store in variable local and domain
        # split local on "+" and keep left side
        # replace "." with ""
        # join local with domain and add to set
        # return count of set

        result = set()

        for email in emails:
            split_email = email.split('@')
            local = split_email[0]
            domain = split_email[1]

            split_local = local.split('+')
            split_local = split_local[0]
            split_local = split_local.replace('.', '')

            final_email = '@'.join([split_local, domain])
            result.add(final_email)

        return len(result)

