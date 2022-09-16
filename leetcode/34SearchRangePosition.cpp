#include <iostream>
#include <vector>

using namespace std;

vector<int> searchRange(vector<int> &nums, int target);

int main()
{
  vector<int> nums{2, 7, 7, 8, 8, 10};
  int target[] = {2, 7, 8, 10, 11};
  int len = 5;

  cout << "Input values: [ ";
  for (const int num : nums)
  {
    cout << num << " ";
  }
  cout << "]" << endl;

  for (int i = 0; i < len; i++)
  {
    cout << endl;
    cout << "Target: " << target[i] << endl;
    vector<int> range = searchRange(nums, target[i]);
    cout << "Range: (" << range.front()
         << ", " << range.back()
         << ")" << endl;
  }

  return 0;
}

vector<int> searchRange(vector<int> &nums, int target)
{
  int minIndex = -1;
  int maxIndex = -1;

  int start = 0;
  int end = nums.size() - 1;

  // max
  while (start <= end)
  {
    int mid = (start + end) / 2;

    if (nums[mid] == target)
    {
      maxIndex = mid;
      start = mid + 1;
    }
    else if (nums[mid] < target)
    {
      start = mid + 1;
    }
    else
    {
      end = mid - 1;
    }
  }

  // min
  start = 0;
  end = nums.size() - 1;

  while (start <= end)
  {
    int mid = (start + end) / 2;

    if (nums[mid] == target)
    {
      minIndex = mid;
      end = mid - 1;
    }
    else if (nums[mid] < target)
    {
      start = mid + 1;
    }
    else
    {
      end = mid - 1;
    }
  }

  return {minIndex, maxIndex};
}